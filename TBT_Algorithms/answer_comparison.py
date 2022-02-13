import numpy as np
import pandas as pd
from transformers import pipeline

checkpoint = "roberta-large-mnli"
pipe = pipeline(task="sentiment-analysis", model=checkpoint, return_all_scores=False)

def answer_accuracy(ans, ref_ans):
    """
    Function compares two answers to see if they're logically compatible.

    Parameters:
    ans: String of answer derived from article that is being tested
    ref_ans: String of answer derived from reference article

    Returns an array containing a Dictionary with a key of the logical relationship (Contradiction, Neutral, Entailment) and a probability value)
    """

    sequences = ref_ans + "</s></s>" + ans
    
    return pipe(sequences)


def answer_accuracy_from_df(df, ref_df):
    """
    Function compares two groups of answers to see if they're logically compatible

    Parameters:
    df: A pandas Series containing Strings of derived answers from tested articles
    ref_df: A pandas Series containing Strings of corresponding answers from reference article

    Returns an array of Dictionaries, each with a key of the logical relationship (Contradiction, Neutral, Entailment) and a probability value)
    """

    df_concat = pd.concat([ref_df, df], axis=1)
    df_processed = df_concat.iloc[:,0] + "</s></s>" + df_concat.iloc[:,1]
    
    sequences = np.expand_dims(df_processed.to_numpy(), -1).tolist()
    
    return pipe(sequences)