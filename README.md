# PneumoniaNet
## Description
Main objective of this program is to classify Pneumonia with deep learning methods. Through this model i hope it can help health workers to automate process classifying Pneumonia throug chest ray image

My main method to make this is using a deep learning approach. I use Convolution Neural Nets to create the classifier and apply transfer learning with pre-trained models. I used Vgg-19 as the backbone 
fine-tune it with my own dataset (which I got from this [Kaggle](https://www.kaggle.com/tolgadincer/labeled-chest-xray-images) link). For the architecture, I used Pytorch as the base framework.

## Installation Guide
For installation options, currently I don't provide the docker image yet. But you can run this simply by clone or fork this repository.

* Clone this repository in your local with this command ```git clone https://github.com/isa96/pneumonia-detection.git```
* Install the requirement modules ```pip install -r requirements.txt```
* If the module already satisfied, you can run the main.py
### Main.py
To use ```main.py```, the model is in ```.pth``` format.
1. See details arguments
```python main.py -h```

2. Perform inference
```python main.py -i <your_image_path> -v <y/n to visualize result>```

## Result
| Input Image      | Output |
| ----------- | ----------- |
| ![Image1](https://github.com/Clayrisee/PneumoniaNet/blob/main/test_image/test_1.jpeg)     | Pneumonia |
| ![Image2](https://github.com/Clayrisee/PneumoniaNet/blob/main/test_image/test_2.jpeg)     | Pneumonia |
| ![Image3](https://github.com/Clayrisee/PneumoniaNet/blob/main/test_image/test_3.jpeg)     | Normal |



