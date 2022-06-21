#Import Libraries
import pandas as pd
import numpy as np
import re

import docx2txt

#Importing additional libraries for ML
import nltk
nltk.download(['wordnet', 'punkt', 'stopwords'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

r_data= docx2txt.process("Sadique_Abdullah_Resume_internship_Rdc.docx")

# # Tokenization function to process your text data

def tokenize(text):
    """
    This function is to process the received messages(text) into usable form.
    it normalizes, tokenize, removes stop-words, lemmatizes, and finally stores clean tokenized word in a list
    """

    # Text Normalization
    text = re.sub("[^a-zA-Z0_9]", " ", str(text))

    # tokenize text
    tokens = word_tokenize(text)

    # Removing stop words
    stop = stopwords.words("english")
    tokens = [w for w in tokens if w not in stop]

    # initiate lemmatizer
    lemmatizer = WordNetLemmatizer()

    # iterate through each token
    clean_tokens = []
    for tok in tokens:
        # lemmatize, normalize case, and remove leading/trailing white space
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

d= tokenize(r_data)
print(d)
print("Number of words in uploaded Resume is ",len(d))
dni = ['sadique', 'mohammad', 'abdullah', 'gmail', 'com', 'linkedin', 'github', 'sadiqueabdullah', '9', 'profile', 'summary',
      'i', 'currently', 'pursuing', 'full', 'time','san', 'francisco', 'seeking','us','of', 'california', 'usa','0','stem',
      'kalinga', 'institute', 'industrial', 'technology', 'bhubaneswar', 'india', 'b', 'tech','00', 'work','present',
      'assistant', 'independent','0k','hindustan', 'aeronautics', 'limited','for', 'playing', 'vital', 'rounder', 'role',
      'bronze','recc', 'honeywell', 'aerospace', 'tempe', 'bangalore', 'senior', 'principal', 'gold', 'being', 'first',]
res = []
for i in d:
    if i not in res and i not in dni:
        res.append(i)

print(res)

print('Number of unique words in uploaded Resume is ',len(res))

# Importing Job description
jd_data= docx2txt.process("JD.docx")
jd= tokenize(jd_data)
print("Total number of of words in JD file is " "", len(jd))

count_jd=len(jd)
print("Number of unique words in JD file is " "",count_jd)

# Number of matching words
def comparator(x,y):
    result = []
    for i in x:
        if i in y:
            result.append(i)
    return result
print(comparator(jd,res))
print("Count of words matching while comparing resume and JD is ",len(comparator(jd,res)))

# Percent of match between JD and resume#
print(f'Current JD and Resume match is {len(comparator(jd,res))/ len(jd)*100:.2f}%')







