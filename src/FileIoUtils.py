<<<<<<< HEAD
from pickle import dump
=======

>>>>>>> e2a77a6fd5406f5f6490567513540f767d68764c

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

<<<<<<< HEAD

    # save a list of clean sentences to file
    def pickle_dump_data(self, sentences, filename):
        dump(sentences, open(filename, 'wb'))
        print('Saved: %s' % filename)




=======
>>>>>>> e2a77a6fd5406f5f6490567513540f767d68764c
