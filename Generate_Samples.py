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

# File Name:		Generate_Samples.py
# Language:		Python general-purpose interpreted high-level programming language.

# This function generates random samples from several multivariate mix of Gaussians, saves the generated data in
# .mat format files and -if enabled- plots the generated data.

# Inputs:
#	plotDistributions:		A boolean to instruct the function to plot the distrbutions generated.
#	numberOfFiles:			An int which specifies the number of mixtures to be generated.

'''
Use example:

	Generate_Samples(True, 1, 10000)
'''


import numpy as np
import matplotlib.pyplot as plt
import Gaussian_Mixture_rnd as gmm
import scipy.io as sio

def Generate_Samples(plotDistributions, numberOfFiles, numberOfSamples):

    if (type(plotDistributions) is not bool) or \
       (type(numberOfFiles) is not int) or \
       (type(numberOfSamples) is not int) or \
       (numberOfSamples <= 0) or \
       (numberOfFiles <= 0) :
        print("In function Generate_Samples: plotDistributions is not bool or "\
              "numberOfFiles is not int or "\
              "numberOfSamples is not int or "\
              "numberOfSamples <= 0 or " \
              "numberOfFiles <= 0")
        raise ValueError('Generate_Samples error')

    # Parameters to generate the mixtures of Gaussians
    n = numberOfSamples
    w = np.array([0.1,0.4,0.1,0.2,0.2])
    mean = np.array([[0,0],[8,8],[2.5,5],[5,-2],[-3,6]])
    cov = np.array([[[5,0],[0,1]],[[4,0],[0,10]],[[2,1],[1,2]],[[2,-1],[-1,2]],[[2,-3],[1,2]]])

    #w = np.array([0.2,0.2,0.1,0.3,0.2])
    #mean = np.array([[0,10],[28,38],[22.25,5],[5,-2],[-33,46]])
    #cov = np.array([[[5,0],[0,1]],[[4,0],[0,10]],[[2,1],[1,2]],[[2,-1],[-1,2]],[[2,-3],[1,2]]])

    for i in range(0,numberOfFiles):
        # Generate training data
        samples, labels = gmm.Gaussian_Mixture_rnd(100*n, w, mean, cov)
    
        print('\n')
        print("Saving training data " + str(i))
    
        data = {'samples': samples,\
                'labels': labels}
    
        fileName = "Training_Data"
        sio.savemat('./' + fileName + str(i), {'data': data})
        print("Traininf data " + str(i) + " saved")
    
        if (plotDistributions) and (i < 1) :
            plt.figure()
            for j in range(0,w.size) :
                indexes = np.where(labels == j)[0]
                sub_samples = samples[indexes,:]
                plt.scatter(sub_samples[:,0], sub_samples[:,1], s=20, marker="*")
    
        plt.title('Training data samples ' + str(i))
    
    
    
    
    
        # Generate inference data
        samples, labels = gmm.Gaussian_Mixture_rnd(n, w, mean, cov)
    
        print('\n')
        print("Saving inference data " + str(i))
    
        data = {'samples': samples,\
                'labels': labels}
    
        fileName = "Inference_Data"
        sio.savemat('./' + fileName + str(i), {'data': data})
        print("Inference data " + str(i) + " saved")
    
        if (plotDistributions) and (i < 1) :
            plt.figure()
            for j in range(0,w.size) :
                indexes = np.where(labels == j)[0]
                sub_samples = samples[indexes,:]
                plt.scatter(sub_samples[:,0], sub_samples[:,1], s=20, marker="+")
    
        plt.title('Inference data samples ' + str(i))
    
    
    
    
    
        # Generate testing data
        samples, labels = gmm.Gaussian_Mixture_rnd(n, w, mean, cov)
    
        print('\n')
        print("Saving testing data " + str(i))
    
        data = {'samples': samples,\
                'labels': labels}
    
        fileName = "Testing_Data"
        sio.savemat('./' + fileName + str(i), {'data': data})
        print("Testing data " + str(i) + " saved")
    
        if (plotDistributions) and (i < 1) :
            plt.figure()
            for j in range(0,w.size) :
                indexes = np.where(labels == j)[0]
                sub_samples = samples[indexes,:]
                plt.scatter(sub_samples[:,0], sub_samples[:,1], s=20, marker="o")
    
        plt.title('Testing data samples ' + str(i))
 
