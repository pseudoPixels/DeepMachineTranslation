# DeepTranslation
[![Sponsors on Open Collective](https://img.shields.io/badge/DeepLearning-TensorFlow-orange.svg?style=flat-square)](#sponsors)
[![Sponsors on Open Collective](https://img.shields.io/badge/DeepLearning-Keras-brightgreen.svg?style=flat-square)](#sponsors)
[![Sponsors on Open Collective](https://img.shields.io/badge/RNN-LSTM-lightgrey.svg?style=flat-square)](#sponsors)
[![Sponsors on Open Collective](https://img.shields.io/badge/Python-3.5-blue.svg?style=flat-square)](#sponsors)
[![Sponsors on Open Collective](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](#sponsors)

DeepTranslation is a Deep Learning based project for automatic machine translation. 


## Example: German To English Translation
Sample automatic translation result (trained on 10,000 sentence pairs):
<p align="center">
  <img src="docs/images/result__trainedOn10000.png" width="100%" title="DeepTranslation">
</p>


Sample automatic translation result (trained on 50,000 sentence pairs):
<p align="center">
  <img src="docs/images/gerEng2.png" width="100%" title="DeepTranslation">
</p>

## Example: Bengali To English Translation
Sample automatic translation result (trained on 4,400 sentence pairs):
<p align="center">
  <img src="docs/images/engBen.png" width="100%" title="DeepTranslation">
</p>


## Installation
```
$ git clone https://github.com/pseudoPixels/DeepTranslation.git
$ cd DeepTranslation
$ pip install -r requirements.txt
```

## Download Trained Model
Some pre-trained model can be downloaded from Google Drive using the following commands:
```
curl -L -o model_4400_Ben2Eng.h5  'https://drive.google.com/uc?export=download&id=1oGosApKUsxJKmrCYKOzegJz-pc1elVm7'
curl -L -o model_10000_Ger2Eng.h5  'https://drive.google.com/uc?export=download&id=16B6mClui1ANYsnmYtdaRWrU0JrSdwjr7'
curl -L -o model_50000_Ger2Eng.h5  'https://drive.google.com/uc?export=download&id=1ZAPwQRIP5M7v8k9hX4MroL_KOnfxsxk9'
```
