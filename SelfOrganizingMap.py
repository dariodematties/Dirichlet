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

# File Name:		SelfOrganizingMap.py
# Language:		Python general-purpose interpreted high-level programming language.

import numpy as np
import Constants as const
import scipy.io as sio
from   scipy   import  spatial as sp
import math

class   SelfOrganizingMap:
    def __init__(self,  unitsArrayDimensionality,
                        inputDimensionality,
                        weightLimits=None):

        self.__updateStep = 0
        self.__inputDimensionality = inputDimensionality
        self._unitsDimensionality = np.prod(np.array(unitsArrayDimensionality)) 
        self._unitsArrayDimensionality = unitsArrayDimensionality

        self.validateObject()

        if const.ENABLE_RANDOM_BEHAVIOUR :
            if weightLimits == None :
                self.__weights = np.random.rand(self._unitsDimensionality,inputDimensionality)
            else :
                self.__weights = np.random.uniform(weightLimits[0],weightLimits[1],(self._unitsDimensionality,inputDimensionality))
        else :
            self.__weights = np.tile(0.5,(self._unitsDimensionality,inputDimensionality))






    def validateObject(self):
        if (type(self.__inputDimensionality) is not int) or \
           (type(self._unitsDimensionality) is not np.int64) or \
           (type(self._unitsArrayDimensionality) is not np.ndarray) :
            print("SelfOrganizingMap object inconsistence: __inputDimensionality is not int or "\
                                                                "_unitsDimensionality is not int or "\
                                                                "_unitsArrayDimensionality is not numpy array")
            raise ValueError('SelfOrganizingMap error')
            
        if (len(self._unitsArrayDimensionality.shape) is not 1) :
            print("SelfOrganizingMap object inconsistence: len(unitsArrayDimensionality.shape) must be one")
            raise ValueError('SelfOrganizingMap error in member function validateObject')
    
        for dim in range(0,self._unitsArrayDimensionality.size): 
            if  type(self._unitsArrayDimensionality[dim]) is not np.int64 :
                print("SelfOrganizingMap object inconsistence: unitsArrayDimensionality in its dim ", dim)
                print("has a wrong value: ", self._unitsArrayDimensionality[dim])
                raise ValueError('SelfOrganizingMap error in member function validateObject')

        if (self.__inputDimensionality == 0) or (self._unitsDimensionality == 0) or (self._unitsArrayDimensionality.size == 0) :
            print("SelfOrganizingMap object inconsistence: inputDimensionality = ", self.__inputDimensionality)
            print("SelfOrganizingMap object inconsistence: unitsArrayDimensionality.size = ", self._unitsArrayDimensionality.size)
            print("SelfOrganizingMap object inconsistence: unitsDimensionality = ", self._unitsDimensionality)
            raise ValueError('SelfOrganizingMap error in member function validateObject')

        for dim in range(0,self._unitsArrayDimensionality.size): 
            if  self._unitsArrayDimensionality[dim] <= 0 :
                print("SelfOrganizingMap object inconsistence: unitsArrayDimensionality in its dim ", dim)
                print("has a wrong value: ", self._unitsArrayDimensionality[dim])
                raise ValueError('SelfOrganizingMap error in member function validateObject')

        product = np.prod(np.array(self._unitsArrayDimensionality))

        if self._unitsDimensionality != product :
                print("SelfOrganizingMap object inconsistence: unitsDimensionality = {} \
                       must be equal to the product of the elements in unitsArrayDimensionality which is = {}".format(self._unitsDimensionality,
                                                                                                                      product))
                raise ValueError('SelfOrganizingMap error in member function validateObject')








    def learningRule(self,learningRate,neighborParameter,unitsWinnerPosition,inputVector):
        if (type(learningRate) is not np.float64) or \
           (type(neighborParameter) is not np.float64) or \
           (type(unitsWinnerPosition) is not np.int64) or \
           (type(inputVector) is not np.ndarray) :
            print("SelfOrganizingMap object inconsistence: learningRate is not np.float64 or "\
                                                                "neighborParameter is not np.float64 or "\
                                                                "unitsWinnerPosition is not np.float64 or "\
                                                                "inputVector is not numpy array")
            raise ValueError('SelfOrganizingMap error in member function learningRule')

        if not (inputVector.size == self.__inputDimensionality) :
            print("SelfOrganizingMap object inconsistence: inputVector.size != __inputDimensionality")
            raise ValueError('SelfOrganizingMap error in member function learningRule')

        for inputElement in inputVector : 
            if  type(inputElement) is not np.float64 :
                print("SelfOrganizingMap object inconsistence: inputElement nside of inputVector is not np.float64")
                raise ValueError('SelfOrganizingMap error in member function learningRule')

        if not (unitsWinnerPosition < self._unitsDimensionality) :
            print("SelfOrganizingMap object inconsistence: unitsWinnerPosition >= _unitsDimensionality")
            raise ValueError('SelfOrganizingMap error in member function learningRule')

        lateralInteractionFunction = 'gaussian'
        neighborhoodValue = self.__learningNeighborhood(neighborParameter, unitsWinnerPosition, lateralInteractionFunction)
        self.__weights+=learningRate*np.transpose(np.tile(neighborhoodValue,(self.__inputDimensionality,1)))*\
                                                 (np.tile(inputVector,(self._unitsDimensionality,1))-self.__weights)








    def __learningNeighborhood(self, widthParameter, winnerPosition, string) :
        if not (winnerPosition < self._unitsDimensionality) :
            print("SelfOrganizingMap object inconsistence: !(winnerPosition < _unitsDimensionality) is true")
            raise ValueError('SelfOrganizingMap error in member function __learningNeighborhood')

        a = np.tile(np.array(np.unravel_index(winnerPosition, self._unitsArrayDimensionality)),(self._unitsDimensionality,1))
        b = np.transpose(np.array(np.unravel_index(range(0,self._unitsDimensionality), self._unitsArrayDimensionality)))
        distances = np.float64(np.sum(np.abs(a-b),axis=1))

        if string == "gaussian" :
            return  np.exp(-(distances**2)/(2*widthParameter))
        else :
            print("SelfOrganizingMap object inconsistence: wrong string")
            raise ValueError('SelfOrganizingMap error in member function __learningNeighborhood')






    def getResponse(self, inputVector) :
        if (type(inputVector) is not np.ndarray) :
            print("SelfOrganizingMap object inconsistence: inputVector is not numpy array")
            raise ValueError('SelfOrganizingMap error in member function getResponse')

        if not (inputVector.size == self.__inputDimensionality) :
                print("SelfOrganizingMap object inconsistence: inputVector.size != __inputDimensionality")
                raise ValueError('SelfOrganizingMap error in member function getResponse')
    
        distances = np.sum(np.abs(self.__weights - np.tile(inputVector,(self._unitsDimensionality,1)))**2,axis=-1)**(1/2)
        return distances, np.argsort(distances)






    def saveStaticSelfOrganizingMapStatus(self, SelfOrganizingMapIdentifier) :
        if not (type(SelfOrganizingMapIdentifier) == str) :
                print("SelfOrganizingMap object inconsistence: SelfOrganizingMapIdentifier is not a string")
                raise ValueError('SelfOrganizingMap error in member function saveStaticSelfOrganizingMapStatus')
    
        string = "SSOM"
        string += SelfOrganizingMapIdentifier

        status = {string + '_inputDimensionality': self.__inputDimensionality,\
                  string + '_unitsDimensionality': self._unitsDimensionality,\
                  string + '_unitsArrayDimensionality': self._unitsArrayDimensionality,\
                  string + '_weights': self.__weights,
                  string + '_updateStep': self.__updateStep}

        return status




    def inference(self, fileName, randomness, sparsity) :
        if (type(sparsity) is not float) :
            print("SelfOrganizingMap object inconsistence: sparsity is not float")
            raise ValueError('SelfOrganizingMap error in member function inference')

        if (sparsity < 0) or (sparsity >= 1) :
            print("SelfOrganizingMap object inconsistence: sparsity must be between 0 and 1")
            raise ValueError('SelfOrganizingMap error in member function inference')

        if (type(fileName) is not str) :
            print("SelfOrganizingMap object inconsistence: fileName is not str")
            raise ValueError('SelfOrganizingMap error in member function inference')

        if (type(randomness) is not bool) :
            print("SelfOrganizingMap object inconsistence: ransomness is not bool")
            raise ValueError('SelfOrganizingMap error in member function inference')

        a = sio.loadmat(fileName)
        samples = a['data'][0][0]['samples']
        if (len(samples.shape) != 2) :
            print("SelfOrganizingMap object inconsistence: len(samples.shape) != 2")
            raise ValueError('SelfOrganizingMap error in member function inference')

        if (samples.shape[1] != self.__inputDimensionality) :
            print("SelfOrganizingMap object inconsistence: samples.shape[1] != self.__inputDimensionality")
            raise ValueError('SelfOrganizingMap error in member function inference')

        labels = a['data'][0][0]['labels']
        if (len(labels.shape) != 2) :
            print("SelfOrganizingMap object inconsistence: len(labels.shape) != 2")
            raise ValueError('SelfOrganizingMap error in member function inference')

        if (labels.shape[0] != 1) or (labels.shape[1] != samples.shape[0]) :
            print("SelfOrganizingMap object inconsistence: labels.shape[0] != 1 or " \
                                                          "labels.shape[1] != samples.shape[0]")
            raise ValueError('SelfOrganizingMap error in member function inference')

        a = None

        outputs = np.zeros((samples.shape[0],self._unitsDimensionality), dtype=bool)
        for i in range(0,samples.shape[0]):
            distances, indexes = self.getResponse(samples[i])
            predisposition = np.reciprocal(distances)
 
            if randomness:
                 predisposition = predisposition**1
                 activeUnits = np.unique(np.random.choice(self._unitsDimensionality, np.int((1.0-sparsity)*self._unitsDimensionality), p=predisposition/np.sum(predisposition)))
            else:
                 activeUnits = np.argsort(predisposition)[0:np.int((1.0-sparsity)*self._unitsDimensionality)]

            np.put(outputs[i],activeUnits,True)

        return outputs, labels

