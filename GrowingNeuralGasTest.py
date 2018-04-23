import numpy as np
import scipy.io as sio
import Generate_Samples as gg
import matplotlib.pyplot as plt
import Add_Noise as nn
import GrowingNeuralGas

numberOfTests = 1
numberOfDimensions = 2

numberOfSamples = 1000
addingNoise = True
plotSamples = True
sparsity = 0.95

gg.Generate_Samples(plotSamples,numberOfTests,numberOfSamples)

if addingNoise :
    nn.Add_Noise(plotSamples,2.0)

randomness = True
iterations = 1
initialNumberOfUnits = 10
initialNumberOfLinks = 5
weightSpan = 1.0
for test in range(0,numberOfTests):

    print('Creatin GNG object for test number ' + str(test))
    GNG = GrowingNeuralGas.GrowingNeuralGas(numberOfDimensions, initialNumberOfUnits, initialNumberOfLinks, weightSpan)
    print('GNG object for test number ' + str(test) + ' created')

    if plotSamples:
        GNG.plotNeuralGas()

    print('\n')
    print('Training Growing Neural Gas Clustering Algorithm number ' + str(test))

    print('Loading Training_Data' + str(test))
    samples = sio.loadmat('./Training_Data' + str(test) + '.mat')['data'][0][0]['samples']
    print('Training_Data' + str(test) + '  loaded')
    numberOfInputs = samples.shape[0];

    print('Processing data for test number ' + str(test))
    for it in range(iterations) :
        for row in range(numberOfInputs) :
            GNG.learning(samples[row])


    if plotSamples:
        GNG.plotNeuralGas()





if plotSamples:
    plt.show()
