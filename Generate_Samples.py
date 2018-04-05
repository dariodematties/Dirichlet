import numpy as np
import matplotlib.pyplot as plt
import Gaussian_Mixture_rnd as gmm

n = 100
w = np.array([0.2,0.3,0.5])
mean = np.array([[0,0],[4,4],[4,1]])
cov = np.array([[[0.1,0],[0,0.1]],[[0.1,0],[0,0.1]],[[0.1,0],[0,0.1]]])

samples, labels = gmm.Gaussian_Mixture_rnd(n, w, mean, cov)

for i in range(0,w.size) :
    indexes = np.where(labels == i)[0]
    sub_samples = samples[indexes,:]
    plt.scatter(sub_samples[:,0], sub_samples[:,1], s=80, marker="*")


plt.show()
