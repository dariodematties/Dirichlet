##################################################################################################################
##				Author:		Dematties Dario Jesus						##
##				Contact:	dariodematties@hotmail.com.ar					##
##						dariodematties@yahoo.com.ar					##
##						dario.dematties@frm.utn.edu.ar					##
##				Project:	Engineering PhD Project						##
##				Institution:	Universidad de Buenos Aires					##
##						Facultad de Ingeniería (FIUBA)					##
##				Workplace:	Instituto de Ingeniería						##
##						Biomédica FIUBA	&						##
##						CCT CONICET Mendoza INCIHUSA					##
##################################################################################################################

# File Name:		GrowingNeuralGas.py
# Language:		Python general-purpose interpreted high-level programming language.

import numpy as np
import Constants as const
import scipy.io as sio
from   scipy   import  spatial as sp
import matplotlib.pyplot as plt
import math

class   GrowingNeuralGas:
    def __init__(self,  inputDimensionality,
                        initialNumberOfUnits,
                        initialNumberOfLinks,
                        weightSpan):

        if (type(inputDimensionality) is not int) or \
           (type(initialNumberOfUnits) is not int) or \
           (type(weightSpan) is not float) or \
           (type(initialNumberOfLinks) is not int) :
            print("GrowingNeuralGas object inconsistence: inputDimensionality is not int or "\
                                                         "initialNumberOfUnits is not int or "\
                                                         "weightSpan is not float or "\
                                                         "initialNumberOfLinks is not int")
            raise ValueError('GrowingNeuralGas error')

        if (inputDimensionality <= 0) or \
           (initialNumberOfUnits <= 0) or \
           (initialNumberOfLinks <= 0) :
            print("GrowingNeuralGas object inconsistence: inputDimensionality <= 0 or "\
                                                         "initialNumberOfUnits <= 0 or "\
                                                         "initialNumberOfLinks <= 0")
            raise ValueError('GrowingNeuralGas error')

        # 0. Start with two units a and b at random positions Wa and Wb in Rn. 
        # I do step 0 differently starting with initialNumberOfUnits units and with initialNumberOfLinks edges among different units
        self.__updateStep = 0
        self.__inputDimensionality = inputDimensionality

        if const.ENABLE_RANDOM_BEHAVIOUR :
            self.__weights = np.random.rand(initialNumberOfUnits,inputDimensionality)*weightSpan
        else :
            self.__weights = np.tile(0.5,(initialNumberOfUnits,inputDimensionality))

        self.__units = np.array(range(0,initialNumberOfUnits))
        self.__edges = np.transpose([np.tile(self.__units, len(self.__units)), np.repeat(self.__units, len(self.__units))])
        self.__edges = np.delete(self.__edges, np.where(self.__edges[:,0] <= self.__edges[:,1]),axis=0)
        np.random.shuffle(self.__edges)
        self.__edges = self.__edges[0:initialNumberOfLinks,:]

        self.__edgeAges = np.zeros(self.__edges.shape[0]).astype(int)
        self.__unitErrors = np.zeros(self.__weights.shape[0]).astype(float)

        self.__removeIsolatedUnits()

        self.__eb = 0.2
        self.__en = 0.006
        self.__lambda = 200
        self.__alpha = 0.5
        self.__d = 0.995
        self.__amax = 50
        






    def plotNeuralGas(self):
        plt.figure()
        plt.scatter(self.__weights[:,0], self.__weights[:,1], s=45, marker="o")
        for i in range(0,self.__edges.shape[0]):
            if self.__inputDimensionality == 2:
                plt.plot([self.__weights[self.__edges[i,0],0],self.__weights[self.__edges[i,1],0]],\
                         [self.__weights[self.__edges[i,0],1],self.__weights[self.__edges[i,1],1]], 'ro-')
            elif self.__inputDimensionality == 3:
                plt.plot([self.__weights[self.__edges[i,0],0],self.__weights[self.__edges[i,1],0]],\
                         [self.__weights[self.__edges[i,0],1],self.__weights[self.__edges[i,1],1]],\
                         [self.__weights[self.__edges[i,0],2],self.__weights[self.__edges[i,1],2]], 'ro-')















    def learning(self, inputVector):
	# 1. Generate an input signal E according to P(E). This sample is in inputVector
        if (type(inputVector) is not np.ndarray) :
            print("GrowingNeuralGas object inconsistence: inputVector is not numpy array")
            raise ValueError('GrowingNeuralGas error in member function getResponse')

        if not (inputVector.size == self.__inputDimensionality) :
                print("GrowingNeuralGas object inconsistence: inputVector.size != __inputDimensionality")
                raise ValueError('GrowingNeuralGas error in member function getResponse')


	# 2. Find the nearest unit s1 and the second-nearest unit s2. 
        distances = np.sum(np.abs(self.__weights - np.tile(inputVector,(self.__units.size,1)))**2,axis=-1)**(1/2)
        indexes = np.argsort(distances)


	# 3. Increment the age of all edges emanating from s1
        edgesIndexes = np.where(self.__edges[:,0] == indexes[0])
        auxiliary = np.where(self.__edges[:,1] == indexes[0])
        neighbors = self.__edges[edgesIndexes,1]
        np.append(neighbors,self.__edges[auxiliary,0])
        np.append(edgesIndexes, auxiliary)

        self.__edgeAges[edgesIndexes] += 1


	# 4. Add the squared distance between the input signal and the nearest unit in
	# input space to a local counter variable:

	# Delta error(s1) = ||w_s1 - E||^2
        self.__unitErrors[indexes[0]] += distances[indexes[0]]**2 


	# 5. Move s1 and its direct topological neighbors towards E by fractions
	# eb and en, respectively, of the total distance:

	# Delta w_s1 = eb(E - w_s1)
	# Delta w_n  = en(E - w_n) for all direct neighbors n of s1
        self.__weights[indexes[0],:] += self.__eb*(inputVector - self.__weights[indexes[0],:])
        self.__weights[neighbors,:] += self.__en*(np.tile(inputVector,(neighbors.size,1)) - self.__weights[neighbors,:])


	# 6. If s1 and s2 are connected by an edge, set the age of this edge to zero. If
	# such an edge does not exist, create it.
        if any(np.sum([indexes[0],indexes[1]] == self.__edges,axis=1)==self.__inputDimensionality):
            self.__edgeAges[np.where(np.sum([indexes[0],indexes[1]] == self.__edges,axis=1)==self.__inputDimensionality)] = 0
        elif any(np.sum([indexes[1],indexes[0]] == self.__edges,axis=1)==self.__inputDimensionality):
            self.__edgeAges[np.where(np.sum([indexes[1],indexes[0]] == self.__edges,axis=1)==self.__inputDimensionality)] = 0
        else:
            self.__edges = np.append(self.__edges,[[indexes[0],indexes[1]]],axis=0)
            self.__edgeAges = np.append(self.__edgeAges,0)


	# 7. Remove edges with an age larger than amax • If this results in points having
	# no emanating edges, remove them as well. 
        self.__edges = np.delete(self.__edges, np.where(self.__edgeAges > self.__amax), axis=0)
        self.__edgeAges = np.delete(self.__edgeAges, np.where(self.__edgeAges > self.__amax))
        self.__removeIsolatedUnits()


	# 8. If the number of input signals generated so far is an integer multiple of a
	# parameter lambda, insert a new unit 
        self.__updateStep += 1
        if np.mod(self.__updateStep, self.__lambda) == 0:
            self.__insertNewUnits()


        # 9. Decrease all error variables by multiplying them with a constant d. 
        self.__unitErrors *= self.__d        


        # 10. If a stopping criterion (e.g., net size or some performance measure) is not
        # yet fulfilled go to step 1. 













    # If there are points having
    # no emanating edges, remove them as well. 
    def __removeIsolatedUnits(self):
        isolatedUnits = np.where(np.isin(self.__units,self.__edges)==False)

        for unit in reversed(isolatedUnits[0]):
            self.__edges[np.where(self.__edges>=unit)] -= 1 

        self.__weights = np.delete(self.__weights, isolatedUnits[0], axis=0)
        self.__unitErrors = np.delete(self.__unitErrors, isolatedUnits[0])
        self.__units = np.arange(self.__units.size - len(isolatedUnits[0]))









    def __insertNewUnits(self):
	# • Determine the unit q with the maximum accumulated error.
        q_index = np.argmax(self.__unitErrors)
	# • Insert a new unit r halfway between q and its neighbor f with the largest error variable: 
	#          w_r = 0.5(w_q + w_f)
        neighbors = np.unique(self.__edges[np.where(self.__edges[:,0]==q_index),1])
        neighbors = np.unique(np.append(neighbors, np.unique(self.__edges[np.where(self.__edges[:,1]==q_index),0])))
        f_index = np.intersect1d(np.where(np.max(self.__unitErrors[neighbors])==self.__unitErrors)[0], neighbors)
        if len(f_index) > 1:
            f_index = np.random.choice(f_index,1)

        self.__weights = np.append(self.__weights, 0.5*(self.__weights[q_index,:] + self.__weights[f_index,:]), axis=0)
        self.__unitErrors = np.append(self.__unitErrors, 0.0)
        self.__units = np.array(range(0,self.__weights.shape[0]))
	# • Insert edges connecting the new unit r with units q and f, and remove
	#   the original edge between q and f.
        self.__edges = np.append(self.__edges, [[self.__weights.shape[0]-1, q_index]], axis=0)
        self.__edgeAges = np.append(self.__edgeAges, 0)
        self.__edges = np.append(self.__edges, [[self.__weights.shape[0]-1, f_index]], axis=0)
        self.__edgeAges = np.append(self.__edgeAges, 0)

        if any(np.sum([q_index,f_index] == self.__edges,axis=1)==self.__inputDimensionality):
            auxiliaryIndex = np.where(np.sum([q_index,f_index] == self.__edges,axis=1)==self.__inputDimensionality)
            self.__edges = np.delete(self.__edges, auxiliaryIndex, axis=0)
            self.__edgeAges = np.delete(self.__edgeAges, auxiliaryIndex)
        elif any(np.sum([f_index,q_index] == self.__edges,axis=1)==self.__inputDimensionality):
            auxiliaryIndex = np.where(np.sum([f_index,q_index] == self.__edges,axis=1)==self.__inputDimensionality)
            self.__edges = np.delete(self.__edges, auxiliaryIndex, axis=0)
            self.__edgeAges = np.delete(self.__edgeAges, auxiliaryIndex)
        else:
            print("GrowingNeuralGas object inconsistence: Trying to remove non-existent edge")
            raise ValueError('GrowingNeuralGas error')

	# • Decrease the error variables of q and f by multiplying them with a
	#   constant alpha. Initialize the error variable of r with the new value of the
	#   error variable of q. 
        self.__unitErrors[q_index] *= self.__alpha
        self.__unitErrors[f_index] *= self.__alpha
        self.__unitErrors[-1] = self.__unitErrors[q_index]



