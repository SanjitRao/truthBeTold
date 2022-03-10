# -*- coding: utf-8 -*-
"""question_generation

text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum \
and first released in 1991, Python's design philosophy emphasizes code \
readability with its notable use of significant whitespace."

text2 = "Gravity (from Latin gravitas, meaning 'weight'), or gravitation, is a natural phenomenon by which all \
things with mass or energy—including planets, stars, galaxies, and even light—are brought toward (or gravitate toward) \
one another. On Earth, gravity gives weight to physical objects, and the Moon's gravity causes the ocean tides. \
The gravitational attraction of the original gaseous matter present in the Universe caused it to begin coalescing \
and forming stars and caused the stars to group together into galaxies, so gravity is responsible for many of \
the large-scale structures in the Universe. Gravity has an infinite range, although its effects become increasingly \
weaker as objects get further away"

text3 = "42 is the answer to life, universe and everything."

text4 = "Forrest Gump is a 1994 American comedy-drama film directed by Robert Zemeckis and written by Eric Roth. \
It is based on the 1986 novel of the same name by Winston Groom and stars Tom Hanks, Robin Wright, Gary Sinise, \
Mykelti Williamson and Sally Field. The story depicts several decades in the life of Forrest Gump (Hanks), \
a slow-witted but kind-hearted man from Alabama who witnesses and unwittingly influences several defining \
historical events in the 20th century United States. The film differs substantially from the novel."
"""

#TODO install the dependencies (then the code below will work!)
'''
!pip install torch
!pip install git+https://github.com/ramsrigouthamg/Questgen.ai
!pip install sense2vec==1.0.3
!pip install git+https://github.com/boudinfl/pke.git

!python -m nltk.downloader universal_tagset
!python -m spacy download en
!wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
!tar -xvf  s2v_reddit_2015_md.tar.gz
!ls s2v_old
'''


from pprint import pprint
import nltk
nltk.download('stopwords')
from Questgen import main
qg= main.QGen()

input_text = '''Biden began his State of the Union address discussing the invasion and said that Putin "badly miscalculated" the Ukrainian people. "Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated," Biden said. "He thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never anticipated or imagined. He met the Ukrainian people." "Throughout our history we’ve learned this lesson when dictators do not pay a price for their aggression they cause more chaos," he added.'''
payload = {
            "input_text": input_text
        }
output = qg.predict_shortq(payload)
pprint (output)






