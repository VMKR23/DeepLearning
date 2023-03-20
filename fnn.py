# -*- coding: utf-8 -*-
"""FNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kZPRlnLR2EVkpLG3XZbots9s_YqKsz29
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

class Feed_Forward_Networks(nn.Module):
    def __init__(self):
        super(Feed_Forward_Networks, self).__init__()
        self.Fullyconnectedlayer1 = nn.Linear(784, 256)
        self.RectifiedLinearUnit1 = nn.ReLU()
        self.Fullyconnectedlayer2 = nn.Linear(256, 128)
        self.RectifiedLinearUnit2 = nn.ReLU()
        self.Fullyconnectedlayer3 = nn.Linear(128, 10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, mp):
        mp = mp.view(-1, 784)
        mp = self.RectifiedLinearUnit1(self.Fullyconnectedlayer1(mp))
        mp = self.RectifiedLinearUnit2(self.Fullyconnectedlayer2(mp))
        mp = self.softmax(self.Fullyconnectedlayer3(mp))
        return mp
train_dataset = datasets.MNIST(root='dataset/', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root='dataset/', train=False, transform=transforms.ToTensor(), download=True)
train_ld = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=128, shuffle=True)
test_ld = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=128, shuffle=False)
model = Feed_Forward_Networks()
optim1 = optim.Adam(model.parameters(), lr=0.003)
criterion = nn.CrossEntropyLoss()
n = 50
loss_1es = []
test_losses = []
m=0
while m<n:
    loss_1 = 0.0
    for i, (imgs, lbls) in enumerate(train_ld):
        outputs = model(imgs)
        loss = criterion(outputs, lbls)
        optim1.zero_grad()
        loss.backward()
        optim1.step()
        loss_1 = loss_1+ loss.item()
    loss_1 = loss_1/len(train_ld)
    loss_1es.append(loss_1)
    test_loss = 0.0
    with torch.no_grad():
        for imgs, lbls in test_ld:
            outputs = model(imgs)
            loss = criterion(outputs, lbls)
            test_loss = test_loss+loss.item()
    test_loss = test_loss/len(test_ld)
    test_losses.append(test_loss)
    print(m+1, n, loss_1, test_loss)
    m+=1
plt.plot(loss_1es, label='Training Loss')
plt.plot(test_losses, label='Test Loss')
plt.xlabel('Training Iterations')
plt.ylabel('Loss')
plt.legend()
plt.show()

