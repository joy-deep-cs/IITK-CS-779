# -*- coding: utf-8 -*-
"""data Visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DYMDm97fWD2cLhjzZmnlJzOr0lpqTasH
"""

!git clone https://github.com/harperco/MeasEval.git

import glob
import pandas as pd

df = pd.concat(map(pd.read_csv, glob.glob('/content/MeasEval/data/trial/tsv/*.tsv')))

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df =  pd.read_csv('/content/MeasEval/data/trial/tsv/S0019103512002801-1342.tsv',delimiter='\t',engine='python')
df = df.sort_values(by = 'startOffset')
df



import spacy
from spacy import displacy
from IPython.core.display import display, HTML
#text = open('/content/MeasEval/data/trial/txt/S0019103512002801-1342.txt', 'r').read()
df.columns = ['docId', 'annotSet', 'label', 'start', 'end','annotId','text','other' ]
ents= df[['label','start','end']].to_dict(orient='records')

ex = [{"text": text,
       "ents": ents,
       "title": None}]
html = displacy.render(ex, style="ent", manual=True)
display(HTML(html))

import os

list = os.listdir('/content/MeasEval/data/trial/txt') # dir is your directory path
number_files = len(list)
number_files

text= 'Rhea is Saturn’s largest icy moon (radius: 1RRh = 764 km). It orbits the planet on an equatorial and circular orbit at a distance of about 8.74Rs from its center (1Rs = 60,268 km).'

text

text







#


