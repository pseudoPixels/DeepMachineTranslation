
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
dataset = obj_fileIO.load_doc("../Datasets/deu-eng/deu.txt")



#transform the dataset in pairs...
dataset_toPairs = obj_dataPrepUtils.to_pairs(dataset)


#clean the datasets (removing punctuations, non-printable and so on)
dataset_clean = obj_dataPrepUtils.clean_pairs(dataset_toPairs)

#pickle save the cleaned dataset
obj_fileIO.pickle_dump_data(dataset_clean, '../Datasets/deu-eng/english-german.pkl')


#load pickle dumped dataset
raw_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german.pkl')


# reduce dataset size
n_sentences = 1000



trainDataset, testDataset = obj_dataPrepUtils.train_test_split(raw_dataset[:n_sentences, :], 0.9)

obj_fileIO.pickle_dump_data(trainDataset, '../Datasets/deu-eng/english-german-train.pkl')
obj_fileIO.pickle_dump_data(testDataset, '../Datasets/deu-eng/english-german-test.pkl')






main_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german.pkl')
train_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german-train.pkl')
test_dataset = obj_fileIO.load_pickle_dump_dataset('../Datasets/deu-eng/english-german-test.pkl')




# prepare english tokenizer
eng_tokenizer = obj_dataPrepUtils.create_tokenizer(main_dataset[:, 0])
eng_vocab_size = len(eng_tokenizer.word_index) + 1
eng_length = obj_dataPrepUtils.max_length(main_dataset[:, 0])
print('English Vocabulary Size: %d' % eng_vocab_size)
print('English Max Length: %d' % (eng_length))


# prepare german tokenizer
ger_tokenizer = obj_dataPrepUtils.create_tokenizer(main_dataset[:, 1])
ger_vocab_size = len(ger_tokenizer.word_index) + 1
ger_length = obj_dataPrepUtils.max_length(main_dataset[:, 1])
print('German Vocabulary Size: %d' % ger_vocab_size)
print('German Max Length: %d' % (ger_length))



# prepare training data
trainX = obj_dataPrepUtils.encode_sequences(ger_tokenizer, ger_length, train_dataset[:, 1])
trainY = obj_dataPrepUtils.encode_sequences(eng_tokenizer, eng_length, train_dataset[:, 0])
trainY = obj_dataPrepUtils.encode_output(trainY, eng_vocab_size)
# prepare validation data
testX = obj_dataPrepUtils.encode_sequences(ger_tokenizer, ger_length, test_dataset[:, 1])
testY = obj_dataPrepUtils.encode_sequences(eng_tokenizer, eng_length, test_dataset[:, 0])
testY = obj_dataPrepUtils.encode_output(testY, eng_vocab_size)





# # define model
model = obj_deepLearner.define_model(ger_vocab_size, eng_vocab_size, ger_length, eng_length, 256)
model.compile(optimizer='adam', loss='categorical_crossentropy')
# summarize defined model
print(model.summary())
#plot_model(model, to_file='model.png', show_shapes=True)
# fit model
filename = 'model.h5'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
model.fit(trainX, trainY, epochs=30, batch_size=64, validation_data=(testX, testY), callbacks=[checkpoint], verbose=2)







# load model
model = obj_fileIO.load_model('model.h5')

obj_deepLearner.evaluate_model(model, eng_tokenizer, trainX, main_dataset)


