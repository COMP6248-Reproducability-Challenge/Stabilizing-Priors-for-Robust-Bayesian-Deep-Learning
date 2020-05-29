import numpy as np
import matplotlib.pyplot as plt

 
train_loss= [358.9673815,148.4768019,113.404618,96.01466146,83.44248024,75.02453544,66.30372481,60.79469905,55.59118463,54.46087288]
tes_loss= [0.225829059,0.382017976,0.107053657,0.332196101,0.159677622,0.138603878,0.117637143,0.087404981,0.140071558,0.057751027]

train_acc = [83.18333333,93.89166667,95.53666667,96.37666667,97.08,97.45666667,97.78833333,97.97666667,98.255,98.30166667]
test_acc = [95.3,96.14,97.19,97.19,97.45,97.61,97.78,97.67,98.08,97.98]
 

x = np.arange(10)

 

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8,6))

 

l1, = ax[0][0].plot(x, train_acc, label="Train Accuracy")
l1, = ax[0][0].plot(x, train_acc, label="Validation Accuracy")

l2, = ax[0][1].plot(x, test_acc, label="Train Loss")
l2, = ax[0][1].plot(x, test_acc, label="Validation Loss")

 
 
ax[0][0].grid(True)
ax[0][1].grid(True)
 
ax[0][0].set_xlabel('Epochs')
ax[0][1].set_xlabel('Epochs')
 

ax[0][0].set_title('Accuracy')
ax[0][1].set_title('Loss')

 

ax[0][0].legend(loc='best', prop={'size': 15})
ax[0][1].legend(loc='best', prop={'size': 15})

 

fig.tight_layout(pad=0.5)

 

plt.savefig('plot.jpg')