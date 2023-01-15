import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import vgg19

class PneumoniaNet(nn.Module):
      
  def __init__(self, output_size):
    super().__init__()
    # Change to true if you wanna to train
    self.vgg19 = vgg19(pretrained=False)
    self.freeze_layer()
    self.vgg19.classifier = nn.Sequential(
    nn.Linear(25088, out_features=4096, bias=True),
    nn.ReLU(inplace=True),
    nn.Dropout(inplace=False),
    nn.Linear(4096, out_features=4096, bias=True),
    nn.ReLU(),
    nn.Dropout(),
    nn.Linear(4096, out_features=output_size),
    nn.LogSoftmax(dim=1)
    )
  
  def forward(self, x):
    x = self.vgg19(x)
    return x

  def freeze_layer(self):
    for param in self.vgg19.parameters():
      param.requires_grad = False
  
  def unfreeze_layer(self):
    for param in self.vgg19.parameters():
      param.requires_grad = True