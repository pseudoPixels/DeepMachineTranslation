import string
import re
from pickle import dump
from unicodedata import normalize
#from numpy import array
import numpy as np


class DataPreprocessingUtils:

    def __init__(self):
        pass

    # split a loaded document into sentences
    def to_pairs(self, doc):
        lines = doc.strip().split('\n')
        pairs = [line.split('\t') for line in lines]
        return pairs



    # clean a list of lines
    def clean_pairs(self, lines):
        cleaned = list()
        # prepare regex for char filtering
        re_print = re.compile('[^%s]' % re.escape(string.printable))
        # prepare translation table for removing punctuation
        table = str.maketrans('', '', string.punctuation)
        for pair in lines:
            clean_pair = list()
            for line in pair:
                # normalize unicode characters
                line = normalize('NFD', line).encode('ascii', 'ignore')
                line = line.decode('UTF-8')
                # tokenize on white space
                line = line.split()
                # convert to lowercase
                line = [word.lower() for word in line]
                # remove punctuation from each token
                line = [word.translate(table) for word in line]
                # remove non-printable chars form each token
                line = [re_print.sub('', w) for w in line]
                # remove tokens with numbers in them
                line = [word for word in line if word.isalpha()]
                # store as string
                clean_pair.append(' '.join(line))
            cleaned.append(clean_pair)
        return np.array(cleaned)


    # clean a list of lines
    def clean_pairs_ben(self, lines):
        cleaned = list()
        # prepare regex for char filtering
        re_print = re.compile('[^%s]' % re.escape(string.printable))
        # prepare translation table for removing punctuation
        table = str.maketrans('', '', string.punctuation)
        for pair in lines:
            clean_pair = list()
            for line in pair:
                # normalize unicode characters
                #line = normalize('NFD', line).encode('ascii', 'ignore')
                #line = line.decode('UTF-8')
                # tokenize on white space
                line = line.split()
                # convert to lowercase
                #line = [word.lower() for word in line]
                # remove punctuation from each token
                #line = [word.translate(table) for word in line]
                # remove non-printable chars form each token
                #line = [re_print.sub('', w) for w in line]
                # remove tokens with numbers in them
                #line = [word for word in line if word.isalpha()]
                # store as string
                clean_pair.append(' '.join(line))
            cleaned.append(clean_pair)
        return np.array(cleaned)