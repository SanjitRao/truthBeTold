from transformers import pipeline

class tinyRobertaQA:
    def __init__(self, checkpoint="deepset/tinyroberta-squad2"):
        self.pipeline = pipeline('question-answering', model=checkpoint, tokenizer=checkpoint)
    
    def answer(self, question, context):
        """
        Function generates an answer based on a question and a context

        Parameters:
        question: String of the question
        context: String of the context to which the answer will be derived fro

        Returns a dictionary including the answer under the "answer" key and the score under the "score" key
        """

        QA_input = {
            'question': question,
            'context': context
        }

        res = self.pipeline(QA_input)
        return res

