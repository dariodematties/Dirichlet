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

# File Name:		Add_Noise.py
# Language:		Python general-purpose interpreted high-level programming language.

# This function generates random samples from several multivariate mix of Gaussians, saves the generated data in
# .mat format files and -if enabled- plots the generated data.

# Inputs:
#	plotDistributions:		A boolean to instruct the function to plot the distrbutions generated.
#	numberOfFiles:			An int which specifies the number of mixtures to be generated.

'''
Use example:

	Add_Noise(0.001)
'''


import numpy as np
import scipy.io as sio
import os.path
import matplotlib.pyplot as plt

def Add_Noise(plotDistributions, noiseAmplitude):
    if (type(noiseAmplitude) is not float):
        print("In function Add_Noise: noiseAmplitude is not float")
        raise ValueError('Add_Noise error')

    if (type(plotDistributions) is not bool):
        print("In function Add_Noise: plotDistributions is not bool")
        raise ValueError('Add_Noise error')

    i=0
    while (os.path.exists('Testing_Data' + str(i) + '.mat')):

        a = sio.loadmat('Testing_Data' + str(i) + '.mat')
        samples = a['data'][0][0]['samples']
        labels = a['data'][0][0]['labels']
        a = None

        if (plotDistributions) and (i < 1) :
            plt.figure()
            for j in np.unique(labels) :
                indexes = np.where(labels == j)[1]
                sub_samples = samples[indexes,:]
                plt.scatter(sub_samples[:,0], sub_samples[:,1], s=20, marker=">")
    
        plt.title('Testing data samples without noise ' + str(i))

        noise = np.random.rand(samples.shape[0],samples.shape[1])*noiseAmplitude
        samples += noise

        data = {'samples': samples,\
                'labels': labels}

        sio.savemat('Testing_Data' + str(i) + '.mat', {'data': data})
    
        if (plotDistributions) and (i < 1) :
            plt.figure()
            for j in np.unique(labels) :
                indexes = np.where(labels == j)[1]
                sub_samples = samples[indexes,:]
                plt.scatter(sub_samples[:,0], sub_samples[:,1], s=20, marker=">")
    
        plt.title('Testing data samples plus noise ' + str(i))
    
        i += 1

