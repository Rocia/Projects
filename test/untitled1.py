#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:10:34 2017

@author: root
"""

import nltk
def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node'):
                print (chunk.node, ' '.join(c[0] for c in chunk.leaves()))
'''                
def extractcontent(filename):
    file = open(filename,'r')
    textt = file.read()
    file.close()
 '''   
text = "Rocia Fernandes is a girl. Machine leaning is a new trend. Aloysius Pinto is a racer."
'''
a = input("Enter your filename (casesensitive):")
extractcontent(a)'''
print(extract_entities(text))
