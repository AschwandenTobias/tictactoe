import torch

x = torch.rand(5, 5)
print(x)
print(torch.cuda.is_available())