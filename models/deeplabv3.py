import torch
import torch.nn as nn
import torch.nn.functional as f

class Deeplabv3(nn.Module):
  def __init__(self, output_stride = 16, num_classes
  
