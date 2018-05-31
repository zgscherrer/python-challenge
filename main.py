import csv
import os
import re
with open('/Users/ZGS/Documents/Data_Bootcamp/Python_homework/python-challenge/PyParagraph/sample_paragraph.csv', 'r', encoding = 'utf8') as f:
    sample_paragraph = f.read()
words = sample_paragraph.split()
sentences = re.split("\.|\?|!", sample_paragraph)
for s in sentences:
    print ("Approximate Word Count: {}".format(len(words)))
    print ("Approximate Sentence Count: {}".format(len(sentences)))
    print ("Average Sentence Length: {}". format(len(words)/float(len(sentences))))
    print ("Approximate Letter Count: {}".format(len(sample_paragraph)/float(len(words))))
    break