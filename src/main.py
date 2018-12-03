
from src.FileIoUtils import *
from src.DataPreprocessingUtils import *












#instantiating the required objects.
obj_fileIO = FileIoUtils()
obj_dataPrepUtils = DataPreprocessingUtils()



dataset = obj_fileIO.load_doc("../Datasets/deu-eng/deu.txt")
dataset_toParis = obj_dataPrepUtils.to_pairs(dataset)




print(dataset_toParis[0])