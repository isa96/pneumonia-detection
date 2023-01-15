from pneumonia_net import PneumoniaNet
import os
import torch
from torchvision import transforms
from PIL import Image
import sys
import argparse
import matplotlib.pyplot as plt

labels = ['NORMAL', 'PNEUMONIA']
PRETRAIN_PATH = os.path.join(os.getcwd(), 'pretrain_weight', 'PneumoniaNet.pth')

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", help="Path Image for input")
parser.add_argument("-v", "--visualize", help="y: if want to visualize the image, n: for no")
args = parser.parse_args()

# Get Image from Image Path
img_path = args.image
image = Image.open(img_path).convert('RGB')

# Preprocess
img_transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
img_transformed = img_transform(image).unsqueeze(0)

# load pretrain model
print(PRETRAIN_PATH)
model = PneumoniaNet(2)
model.load_state_dict(torch.load(PRETRAIN_PATH,  map_location=torch.device('cpu')))
print(model)

with torch.no_grad():
    model.eval()
    output = model(img_transformed)


#Visualize Model
if args.visualize =='y':
    plt.imshow(image), plt.xticks([]), plt.yticks([])
    plt.xlabel("Predicted class is: {}".format(labels[output.argmax()]))
    plt.show()
else:
    print("Predicted class is: {}".format(labels[output.argmax()]))