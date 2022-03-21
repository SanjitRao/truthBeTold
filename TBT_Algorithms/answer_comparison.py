import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


#TODO: 1) Create a string of all news orgs you wanna pull from (or is this actually necessary?)
#      2)

# from Preprocessing import sentence_tokenizer
# ans = sentence_tokenizer() #sentence tokenizes the base article
# from NewsAPI import keyword_NS_searchAlg_V2, BoW_Topic_Identification
# ref_ans = ""

class MNLIComparator:
    def __init__(self, checkpoint="roberta-large-mnli"):
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

    def compare(self, ans, ref_ans):
        """
        Function compares two answers to see if they're logically compatible. It tests whether ans is true given ref_ans.

        Parameters:
        ans: String or array of strings of answer(s) derived from article that is being tested
        ref_ans: String or array of strings of the corresponding answer(s) derived from reference article

        Returns an array of arrays, each containing the softmaxed probabilities of Contradiction, Neutral, and Entailment at indices 0, 1, and 2 respectively
        """

        tokens = self.tokenizer(ans, ref_ans, padding=True, truncation=True, return_tensors="pt")
        outputs = self.model(**tokens)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

        return predictions


class MiniLMComparator:
    def __init__(self, checkpoint='sentence-transformers/paraphrase-MiniLM-L6-v2'):
        self.model = SentenceTransformer(checkpoint)

    def compareStrings(self, ans, ref_ans):
        """
        Function compares answers to see if they are paraphrases of each other. It is commutative.

        Parameteres:
        ans: String derived from article that is being tested
        ref_ans: String of the corresponding answer(s) derived from reference article

        Returns an array of arrays containing the probability of the pair of sentences being paraphrases of each other
        """

        ans_array = [ans]
        ref_ans_array = [ref_ans]
        return self.compareArrays(ans_array, ref_ans_array)

    def compareArrays(self, ans, ref_ans):
        """
        Function compares answers to see if they are paraphrases of each other. It is commutative.

        Parameteres:
        ans: Array of strings of answer(s) derived from article that is being tested
        ref_ans: Array of strings of the corresponding answer(s) derived from reference article

        Returns an array of arrays, each containing the probability of a pair of sentences being paraphrases of each other
        """

        embeddings = self.model.encode(ans)
        ref_embeddings = self.model.encode(ref_ans)
        similarities = cosine_similarity(embeddings, ref_embeddings) # dense output

        return similarities

"""
@article{liu2019roberta,
    title = {RoBERTa: A Robustly Optimized BERT Pretraining Approach},
    author = {Yinhan Liu and Myle Ott and Naman Goyal and Jingfei Du and
              Mandar Joshi and Danqi Chen and Omer Levy and Mike Lewis and
              Luke Zettlemoyer and Veselin Stoyanov},
    journal={arXiv preprint arXiv:1907.11692},
    year = {2019},
}

@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "http://arxiv.org/abs/1908.10084",
}
"""