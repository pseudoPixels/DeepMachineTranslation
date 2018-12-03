class DataPreprocessingUtils:

    def __init__(self):
        pass

    # split a loaded document into sentences
    def to_pairs(self, doc):
        lines = doc.strip().split('\n')
        pairs = [line.split('\t') for line in lines]
        return pairs

