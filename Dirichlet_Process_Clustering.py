##################################################################################################################
##                                Author:                Dematties Dario Jesus                                  ##
##                                Contact:        dariodematties@hotmail.com.ar                                 ##
##                                                dariodematties@yahoo.com.ar                                   ##
##                                                dario.dematties@frm.utn.edu.ar                                ##
##                                Project:        Engineering PhD Project                                       ##
##                                Institution:        Universidad de Buenos Aires                               ##
##                                                Facultad de Ingeniería (FIUBA)                                ##
##                                Workplace:        Instituto de Ingeniería                                     ##
##                                                Biomédica FIUBA        &                                      ##
##                                                CCT CONICET Mendoza INCIHUSA                                  ##
##################################################################################################################

# File Name:                Dirichlet_Process_clustering.py
# Language:                Python general-purpose interpreted high-level programming language.

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Dirichlet_Process_Clustering:

#   This is the object constructor
#   This function creates an object of class Dirichlet_Process_clustering
    def __init__(self,  num_processes,
                        num_weights,
                        num_dimensions,
                        alpha):

        self.__num_processes = num_processes
        self.__num_weights = num_weights
        self.__num_dimensions = num_dimensions
        self.__alpha = alpha

        self.__validateObject()

        self.__weights = []
        self.__coordinates = []


#   This function validates an object created of class Dirichlet_Process_clustering
    def __validateObject(self):
        if (type(self.__num_processes) is not int) or \
           (type(self.__num_weights) is not int) or \
           (type(self.__num_dimensions) is not int) or \
           (type(self.__alpha) is not np.float) :
            print("Dirichlet_Process_clustering object inconsistence: __num_processes is not int or "\
                                                                     "__num_weights is not int or "\
                                                                     "__num_dimensions is not int or "\
                                                                     "__alpha is not float")
            raise ValueError('Dirichlet_Process_clustering error')

        if (self.__num_processes <= 0) or (self.__num_weights <= 0)  or (self.__num_dimensions <= 0) or (self.__alpha <= 0) :
            print("Dirichlet_Process_clustering object inconsistence: num_processes = ", self.__num_processes)
            print("Dirichlet_Process_clustering object inconsistence: num_weights = ", self.__num_weights)
            print("Dirichlet_Process_clustering object inconsistence: num_dimensions = ", self.__num_dimensions)
            print("Dirichlet_Process_clustering object inconsistence: alpha = ", self.__alpha)
            raise ValueError('Dirichlet_Process_clustering error in member function validateObject')


#   This function generates random samples from the Dirichlet process through the stick breaking method.
#   Those random samples are probability mass functions (pmf).
    def __Stick_breaking_process(self):
        # computes a vector with all betas
        betas = np.random.beta(1, self.__alpha, self.__num_weights-1)
        # computes a vector with all remaining stick lengths
        remaining_stick_lengths = np.cumprod(1-betas)
        return np.append(betas, 1)*np.append(1, remaining_stick_lengths)


#   This function trains the clustering algorithm
    def train(self, fileName):
        if (type(fileName) is not str) :
            print("Dirichlet_Process_clustering object inconsistence: fileName is not str")
            raise ValueError('Dirichlet_Process_clustering error in member function train')

        samples = sio.loadmat(fileName)['data'][0][0]['samples']
        if (len(samples.shape) != 2) :
            print("Dirichlet_Process_clustering object inconsistence: len(samples.shape) != 2")
            raise ValueError('Dirichlet_Process_clustering error in member function train')

        if (samples.shape[0] != self.__num_weights) or (samples.shape[1] != self.__num_dimensions) :
            print("Dirichlet_Process_clustering object inconsistence: samples.shape[0] != self.__num_weights or " \
                                                                     "samples.shape[1] != self.__num_dimensions")
            raise ValueError('Dirichlet_Process_clustering error in member function train')

        for process in range(0,self.__num_processes) :
            auxiliary = self.__Stick_breaking_process() 
            indexes = np.where(auxiliary > np.mean(auxiliary)/100)
            if process == 0 :
                self.__weights = auxiliary[indexes]
                indexes = np.random.choice(range(0,self.__num_weights),indexes[0].size)
                self.__coordinates = samples[indexes]
            else :
                self.__weights = np.append(self.__weights,auxiliary[indexes])
                indexes = np.random.choice(range(0,self.__num_weights),indexes[0].size)
                self.__coordinates = np.append(self.__coordinates,samples[indexes],axis=0)

        if (self.__num_processes == 1) and (self.__num_dimensions == 2) :
            self.__Plot_Points(self.__coordinates[:,0], self.__coordinates[:,1], self.__weights)













#   This function makes inference from the testing data
    def inference(self, fileName, randomness, sparsity):
        if (type(sparsity) is not float) :
            print("Dirichlet_Process_clustering object inconsistence: sparsity is not float")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        if (sparsity < 0) or (sparsity >= 1) :
            print("Dirichlet_Process_clustering object inconsistence: sparsity must be between 0 and 1")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        if (type(fileName) is not str) :
            print("Dirichlet_Process_clustering object inconsistence: fileName is not str")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        if (type(randomness) is not bool) :
            print("Dirichlet_Process_clustering object inconsistence: ransomness is not bool")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        a = sio.loadmat(fileName)
        samples = a['data'][0][0]['samples']
        if (len(samples.shape) != 2) :
            print("Dirichlet_Process_clustering object inconsistence: len(samples.shape) != 2")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        if (samples.shape[1] != self.__num_dimensions) :
            print("Dirichlet_Process_clustering object inconsistence: samples.shape[1] != self.__num_dimensions")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        labels = a['data'][0][0]['labels']
        if (len(labels.shape) != 2) :
            print("Dirichlet_Process_clustering object inconsistence: len(labels.shape) != 2")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        if (labels.shape[0] != 1) or (labels.shape[1] != samples.shape[0]) :
            print("Dirichlet_Process_clustering object inconsistence: labels.shape[0] != 1 or " \
                                                                     "labels.shape[1] != samples.shape[0]")
            raise ValueError('Dirichlet_Process_clustering error in member function inference')

        a = None

        outputs = np.zeros((samples.shape[0],self.__weights.size), dtype=bool)
        for i in range(0,samples.shape[0]):
            distances = np.sum(np.abs(self.__coordinates - np.tile(samples[i],(self.__weights.size,1)))**2,axis=-1)**(1/2)
            predisposition = np.reciprocal(distances)*self.__weights
 
            if randomness:
                 predisposition = predisposition**1
                 activeUnits = np.unique(np.random.choice(self.__weights.size, np.int((1.0-sparsity)*self.__weights.size), p=predisposition/np.sum(predisposition)))
            else:
                 activeUnits = np.flip(np.argsort(predisposition),axis=0)[0:np.int((1.0-sparsity)*self.__weights.size)]

            np.put(outputs[i],activeUnits,True)

        return outputs, labels











#   This is a private function to plot the Dirichlet Process Clustering.
#   This function does not make argument error checking, then passing the correct arguments is a complete
#   responsibility from the method that call it inside the class
    def __Plot_Points(self, xpos, ypos, zvalues):

        plt.figure()
        marker_size=15
        plt.scatter(np.flip(xpos,axis=0), np.flip(ypos,axis=0), marker_size, c=np.flip(zvalues,axis=0), cmap='jet')
        plt.title("Dirichlet Proces Clustering (Stick breaking)")
        plt.xlabel("Dimension 1")
        plt.ylabel("Dimension 2")
        cbar= plt.colorbar()
        cbar.set_label("Weights", labelpad=+1)





