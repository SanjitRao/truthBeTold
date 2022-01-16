'''from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("xlnet-base-cased")
model = AutoModel.from_pretrained("xlnet-base-cased")

inputs = tokenizer("Hello world!", return_tensors="pt")
outputs = model(**inputs)'''
#+--------------------------------------------------------------+#


###                                    For STS Dataset
import pandas as pd
import numpy as np
import scipy
import math
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
##                                    For SICK Dataset
import requests
##                                    For Preparation
import nltk
import gensim
from gensim.models import Word2Vec
from gensim.scripts.glove2word2vec import glove2word2vec
from sklearn.metrics.pairwise import cosine_similarity ##cosine_similarity is here
from collections import Counter
import math
##                                    For Smooth Inverse Frequency
from sklearn.decomposition import TruncatedSVD
##                                    For Google Pretrained Sentence Encoder
import tensorflow_hub as hub

def load_sts_dataset(filename):
    # Loads a subset of the STS dataset into a DataFrame. In particular both
    # sentences and their human rated similarity score.
    sent_pairs = []
    with tf.gfile.GFile(filename, "r") as f:
        for line in f:
            ts = line.strip().split("\t")
            sent_pairs.append((ts[5], ts[6], float(ts[4])))
    return pd.DataFrame(sent_pairs, columns=["sent_1", "sent_2", "sim"])


def download_and_load_sts_data():
    sts_dataset = tf.keras.utils.get_file(
        fname="Stsbenchmark.tar.gz",
        origin="http://ixa2.si.ehu.es/stswiki/images/4/48/Stsbenchmark.tar.gz",
        extract=True)

    sts_dev = load_sts_dataset(os.path.join(os.path.dirname(sts_dataset), "stsbenchmark", "sts-dev.csv"))
    sts_test = load_sts_dataset(os.path.join(os.path.dirname(sts_dataset), "stsbenchmark", "sts-test.csv"))

    return sts_dev, sts_test

sts_dev, sts_test = download_and_load_sts_data()

##                                        SICK Dataset

def download_sick(f):
    response = requests.get(f).text

    lines = response.split("\n")[1:]
    lines = [l.split("\t") for l in lines if len(l) > 0]
    lines = [l for l in lines if len(l) == 5]

    df = pd.DataFrame(lines, columns=["idx", "sent_1", "sent_2", "sim", "label"])
    df['sim'] = pd.to_numeric(df['sim'])
    return df

sick_train = download_sick("https://raw.githubusercontent.com/alvations/stasis/master/SICK-data/SICK_train.txt")
sick_dev = download_sick("https://raw.githubusercontent.com/alvations/stasis/master/SICK-data/SICK_trial.txt")
sick_test = download_sick("https://raw.githubusercontent.com/alvations/stasis/master/SICK-data/SICK_test_annotated.txt")
sick_all = sick_train.append(sick_test).append(sick_dev)

##                                Preparation
STOP = set(nltk.corpus.stopwords.words("english"))

# Sentence class
class Sentence:

    def __init__(self, sentence):
        self.raw = sentence
        normalized_sentence = sentence.replace("‘", "'").replace("’", "'")
        self.tokens = [t.lower() for t in nltk.word_tokenize(normalized_sentence)]
        self.tokens_without_stop = [t for t in self.tokens if t not in STOP]

PATH_TO_WORD2VEC = os.path.expanduser("~/data/word2vec/GoogleNews-vectors-negative300.bin")
PATH_TO_GLOVE = os.path.expanduser("~/data/glove/glove.840B.300d.txt")
word2vec = gensim.models.KeyedVectors.load_word2vec_format(PATH_TO_WORD2VEC, binary=True)

#loading Glove
tmp_file = "/tmp/glove.840B.300d.w2v.txt"
glove2word2vec(PATH_TO_GLOVE, tmp_file)
glove = gensim.models.KeyedVectors.load_word2vec_format(tmp_file)
import csv

PATH_TO_FREQUENCIES_FILE = "data/sentence_similarity/frequencies.tsv"
PATH_TO_DOC_FREQUENCIES_FILE = "data/sentence_similarity/doc_frequencies.tsv"

def read_tsv(f):
    frequencies = {}
    with open(f) as tsv:
        tsv_reader = csv.reader(tsv, delimiter="\t")
        for row in tsv_reader:
            frequencies[row[0]] = int(row[1])
    return frequencies

frequencies = read_tsv(PATH_TO_FREQUENCIES_FILE)
doc_frequencies = read_tsv(PATH_TO_DOC_FREQUENCIES_FILE)
doc_frequencies["NUM_DOCS"] = 1288431

## SMOOTH INVERSE FREQUENCY
def remove_first_principal_component(X):
    svd = TruncatedSVD(n_components=1, n_iter=7, random_state=0)
    svd.fit(X)
    pc = svd.components_
    XX = X - X.dot(pc.transpose()) * pc
    return XX

#model = word2vec ******************************************
def run_sif_benchmark(sentences1, sentences2, model, freqs={}, use_stoplist=False, a=0.001):
    total_freq = sum(freqs.values())
    embeddings = []
    # SIF requires us to first collect all sentence embeddings and then perform
    # common component analysis.
    for (sent1, sent2) in zip(sentences1, sentences2):
        tokens1 = sent1.tokens_without_stop if use_stoplist else sent1.tokens
        tokens2 = sent2.tokens_without_stop if use_stoplist else sent2.tokens

        tokens1 = [token for token in tokens1 if token in model]
        tokens2 = [token for token in tokens2 if token in model]

        weights1 = [a / (a + freqs.get(token, 0) / total_freq) for token in tokens1]
        weights2 = [a / (a + freqs.get(token, 0) / total_freq) for token in tokens2]

        embedding1 = np.average([model[token] for token in tokens1], axis=0, weights=weights1)
        embedding2 = np.average([model[token] for token in tokens2], axis=0, weights=weights2)

        embeddings.append(embedding1)
        embeddings.append(embedding2)
    embeddings = remove_first_principal_component(np.array(embeddings))
    sims = [cosine_similarity(embeddings[idx * 2].reshape(1, -1),
                              embeddings[idx * 2 + 1].reshape(1, -1))[0][0]
            for idx in range(int(len(embeddings) / 2))]
    return sims

#Google Sentence Encoder
tf.logging.set_verbosity(tf.logging.ERROR)
embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/1")

def run_gse_benchmark(sentences1, sentences2):
    sts_input1 = tf.placeholder(tf.string, shape=(None))
    sts_input2 = tf.placeholder(tf.string, shape=(None))

    sts_encode1 = tf.nn.l2_normalize(embed(sts_input1))
    sts_encode2 = tf.nn.l2_normalize(embed(sts_input2))

    sim_scores = tf.reduce_sum(tf.multiply(sts_encode1, sts_encode2), axis=1)
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        [gse_sims] = session.run(
            [sim_scores],
            feed_dict={
                sts_input1: [sent1.raw for sent1 in sentences1],
                sts_input2: [sent2.raw for sent2 in sentences2]
            })
    return gse_sims


def maxSimSIF_Google(sim1, sim2): #sim1 and sim2 are 1 item lists
    if(sim1[0] >=sim2[0]):
        return sim1[0]
    return sim2[0]


#-------------------------------------------------------------------------------------------------------\
import transformers
import nltk
nltk.download('punkt')
import nlp

## ansT5,ansSQ = Sentence(ansT5), Sentence(ansSQ)
##model = word2vec
#sims_ansSIF =  run_sif_benchmark(ansT5, ansSQ, model, freqs = frequencies, a = 0.001)
#sims_ansGoog = run_gse_benchmark(ansT5, ansSQ)
##checking if t5 answer similar to Squad answer: maxSimSIF_Google(sims_ansSIF, sims_ansGoog)
#-------------------------------------------------------------------------------------------------------
