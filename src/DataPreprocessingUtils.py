
import string
import re
from pickle import dump
from unicodedata import normalize
#from numpy import array
import numpy as np


from pickle import load
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.utils.vis_utils import plot_model
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from keras.callbacks import ModelCheckpoint



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

                line = line.encode().decode()
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



    def train_test_split(self, dataset, splitRatio):
        numSamples = len(dataset)
        numTrainDataset = int(numSamples*splitRatio)

        #print(numTrainDataset)

        np.random.shuffle(dataset)

        #print(dataset)


        return dataset[:numTrainDataset], dataset[numTrainDataset:]





    # fit a tokenizer
    def create_tokenizer(self, lines):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(lines)
        return tokenizer


    # max sentence length
    def max_length(self, lines):
        return max(len(line.split()) for line in lines)



    # encode and pad sequences
    def encode_sequences(self, tokenizer, length, lines):
        # integer encode sequences
        X = tokenizer.texts_to_sequences(lines)
        # pad sequences with 0 values
        X = pad_sequences(X, maxlen=length, padding='post')
        return X


    # one hot encode target sequence
    def encode_output(self, sequences, vocab_size):
        ylist = list()
        for sequence in sequences:
            encoded = to_categorical(sequence, num_classes=vocab_size)
            ylist.append(encoded)
        y = array(ylist)
        y = y.reshape(sequences.shape[0], sequences.shape[1], vocab_size)
        return y
