
from src.FileIoUtils import *
from src.DataPreprocessingUtils import *













#instantiating the required objects.
obj_fileIO = FileIoUtils()
obj_dataPrepUtils = DataPreprocessingUtils()


#load dataset...
#======>>> Bengali 2 English: "../Datasets/ben-eng/ben.txt"
#======>>> German 2 English: "../Datasets/deu-eng/deu.txt"
dataset = obj_fileIO.load_doc("../Datasets/deu-eng/deu.txt")



#transform the dataset in pairs...
dataset_toPairs = obj_dataPrepUtils.to_pairs(dataset)


#clean the datasets (removing punctuations, non-printable and so on)
dataset_clean = obj_dataPrepUtils.clean_pairs(dataset_toPairs)

#pickle save the cleaned dataset
#obj_fileIO.pickle_dump_data(dataset_clean, '../Datasets/deu-eng/english-german.pkl')


#load pickle dumped dataset
raw_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german.pkl')


obj_dataPrepUtils.train_test_split(raw_dataset[:50, :], 0.5)





