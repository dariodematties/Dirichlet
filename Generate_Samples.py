import numpy as np
import matplotlib.pyplot as plt
import Gaussian_Mixture_rnd as gmm
import scipy.io as sio

n = 10000
w = np.array([0.1,0.6,0.05,0.25])
mean = np.array([[0,0],[4,4],[4,1],[1,4]])
cov = np.array([[[5,0],[0,1]],[[4,0],[0,10]],[[2,1],[1,2]],[[2,-1],[-1,2]]])

samples, labels = gmm.Gaussian_Mixture_rnd(n, w, mean, cov)

print("Saving data")

data = {'samples': samples,\
        'labels': labels}

fileName = "Data"
sio.savemat('./' + fileName, {'data': data})
print("Data saved")

for i in range(0,w.size) :
    indexes = np.where(labels == i)[0]
    sub_samples = samples[indexes,:]
    plt.scatter(sub_samples[:,0], sub_samples[:,1], s=20, marker="*")


plt.show()


