import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import Generate_Samples as gg
import Add_Noise as nn
import Dirichlet_Process_Clustering as dp

numberOfTests = 5
numberOfSamples = 1000
addingNoise = True
plotSamples = True
sparsity = 0.99

gg.Generate_Samples(plotSamples,numberOfTests,numberOfSamples)

if addingNoise :
    nn.Add_Noise(plotSamples,4.0)

numberOfProcesses = 1
numberOfDimensions = 2
alpha = 1000.0
DC = dp.Dirichlet_Process_Clustering(numberOfProcesses,100*numberOfSamples,numberOfDimensions,alpha)

randomness = True
for test in range(0,numberOfTests):
    print('\n')
    print('Training Dirichlet Process Clustering Algorithm number ' + str(test))
    DC.train('Training_Data' + str(test))

    # Generate Inference data
    print('\n')
    print('Generating inference data ' + str(test))
    SDRs, tags = DC.inference('Inference_Data' + str(test), randomness, sparsity)

    print("Saving inference output " + str(test))
    
    data = {'SDRs': SDRs,\
            'tags': tags}
    
    fileName = "Inference_Output_Data"
    sio.savemat('./' + fileName + str(test), {'data': data})
    print("Inference output data " + str(test) + " saved")



    # Generate Testing data
    print('\n')
    print('Generating testing data ' + str(test))
    SDRs, tags = DC.inference('Testing_Data' + str(test), randomness, sparsity)

    print("Saving testing output " + str(test))
    
    data = {'SDRs': SDRs,\
            'tags': tags}
    
    fileName = "Testing_Output_Data"
    sio.savemat('./' + fileName + str(test), {'data': data})
    print("Testing output data " + str(test) + " saved")


if (numberOfTests == 1):
    plt.show()
