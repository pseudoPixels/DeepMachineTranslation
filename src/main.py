# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, mode='rt', encoding='utf-8')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


loadedDataset = load_doc('../Datasets/deu-eng/deu.txt')

print(loadedDataset)
