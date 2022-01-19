
from pipelines import pipeline
nlp = pipeline("e2e-qg")
nlp("Python is a programming language. Created by Guido van Rossum and first released in 1991.")

#### INFERENCE DATABASE  ###
inference_test_list = ['Socrates is a man', 'All men are mortal']
p1 = read_expr('man(socrates)')
p2 = read_expr('all x.(man(x) -> mortal(x))')
c  = read_expr('mortal(socrates)')
Prover9().prove(c, [p1,p2]) #Uses Prover9 to logically infer that Socrates is mortal
## TODO: Need a way to convert Strings into Expressions


## TODO: make a copy of database_list, make each item an expression, set up Prover9 and equiv()