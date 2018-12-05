
from pickle import load
from pickle import dump
from keras.models import load_model




class FileIoUtils:

    def __init__(self):
        pass

    # load dataset text file
    def load_doc(self, filename):
        # open the file as read only
        file = open(filename, mode='rt', encoding='utf-8')
        # read all text
        text = file.read()
        # close the file
        file.close()
        return text



    # save a list of clean sentences to file
    def pickle_dump_data(self, sentences, filename):
        dump(sentences, open(filename, 'wb'))
        print('Saved: %s' % filename)


    # load a clean dataset
    def load_pickle_dump_dataset(self, filename):
        return load(open(filename, 'rb'))


    def load_model(self, fileName):
        return load_model(fileName)


