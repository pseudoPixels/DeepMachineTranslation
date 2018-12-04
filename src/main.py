
from src.FileIoUtils import *
from src.DataPreprocessingUtils import *
from src.DeepLearner import *













#instantiating the required objects.
obj_fileIO = FileIoUtils()
obj_dataPrepUtils = DataPreprocessingUtils()
obj_deepLearner = DeepLearner()


#load dataset...
#======>>> Bengali 2 English: "../Datasets/ben-eng/ben.txt"
#======>>> German 2 English: "../Datasets/deu-eng/deu.txt"
##dataset = obj_fileIO.load_doc("../Datasets/deu-eng/deu.txt")



#transform the dataset in pairs...
##dataset_toPairs = obj_dataPrepUtils.to_pairs(dataset)


#clean the datasets (removing punctuations, non-printable and so on)
##dataset_clean = obj_dataPrepUtils.clean_pairs(dataset_toPairs)

#pickle save the cleaned dataset
#obj_fileIO.pickle_dump_data(dataset_clean, '../Datasets/deu-eng/english-german.pkl')


#load pickle dumped dataset
#raw_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german.pkl')


# reduce dataset size
##n_sentences = 100



##trainDataset, testDataset = obj_dataPrepUtils.train_test_split(raw_dataset[:n_sentences, :], 0.9)

##obj_fileIO.pickle_dump_data(trainDataset, '../Datasets/deu-eng/english-german-train.pkl')
##obj_fileIO.pickle_dump_data(testDataset, '../Datasets/deu-eng/english-german-test.pkl')






main_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german.pkl')
train_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german-train.pkl')
test_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german-test.pkl')







