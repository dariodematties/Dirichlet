import numpy as np
import scipy.io as sio
import Generate_Samples as gg
import Add_Noise as nn
import SelfOrganizingMap

numberOfTests = 5
numberOfDimensions = 2
dim = 32
unitsArrayDimensionality = np.array([dim,dim,4])


numberOfSamples = 1000
addingNoise = True
plotSamples = True
sparsity = 0.95

gg.Generate_Samples(plotSamples,numberOfTests,numberOfSamples)

if addingNoise :
    nn.Add_Noise(plotSamples,2.0)

randomness = True
iterations = 1
for test in range(0,numberOfTests):

    print('Creatin SOM object for test number ' + str(test))
    SOM = SelfOrganizingMap.SelfOrganizingMap(unitsArrayDimensionality,numberOfDimensions)
    print('SOM object for test number ' + str(test) + ' created')

    print('\n')
    print('Training Self Organizing Map Clustering Algorithm number ' + str(test))

    print('Loading Training_Data' + str(test))
    samples = sio.loadmat('./Training_Data' + str(test) + '.mat')['data'][0][0]['samples']
    print('Training_Data' + str(test) + '  loaded')
    numberOfInputs = samples.shape[0];

    print('Processing data for test number ' + str(test))
    for it in range(iterations) :
        for row in range(numberOfInputs) :
            learningRate = np.float64(0.9*(0.01/0.9))**(np.float64(row+it*numberOfInputs)/np.float64(numberOfInputs*iterations))
            neighborParameter = np.float64(5*0.01)**(np.float64(row+it*numberOfInputs)/np.float64(numberOfInputs*iterations))
            unitsWinnerPosition = SOM.getResponse(samples[row])[1][0];
            SOM.learningRule(learningRate, neighborParameter, unitsWinnerPosition, samples[row]);

    for it in range(iterations) :
        for row in range(numberOfInputs) :
            learningRate = np.float64(0.1*(0.01/0.9))**(np.float64(row+it*numberOfInputs)/np.float64(numberOfInputs*iterations))
            neighborParameter = np.float64(0.5*0.01)**(np.float64(row+it*numberOfInputs)/np.float64(numberOfInputs*iterations))
            unitsWinnerPosition = SOM.getResponse(samples[row])[1][0];
            SOM.learningRule(learningRate, neighborParameter, unitsWinnerPosition, samples[row]);

    learningRate = np.float64(0.1*(0.01/0.9))
    neighborParameter = np.float64(0.5*0.01)
    for it in range(iterations) :
        for row in range(numberOfInputs) :
            unitsWinnerPosition = SOM.getResponse(samples[row])[1][0];
            SOM.learningRule(learningRate, neighborParameter, unitsWinnerPosition, samples[row]);

    print('Data processed')

    if (test == 0) :
        print('Saving object status number ' + str(test))
        SelfOrganizingMapIdentifier='1'
        fileName = 'SOM_Status'
        status=SOM.saveStaticSelfOrganizingMapStatus(SelfOrganizingMapIdentifier)
        sio.savemat('./' + fileName, {'status': status})
        print('Object status number ' + str(test) + '  saved')




    # Generate Inference data
    print('\n')
    print('Generating inference data ' + str(test))
    SDRs, tags = SOM.inference('Inference_Data' + str(test), randomness, sparsity)

    print('Saving inference output ' + str(test))
    
    data = {'SDRs': SDRs,\
            'tags': tags}
    
    fileName = 'Inference_Output_Data'
    sio.savemat('./' + fileName + str(test), {'data': data})
    print('Inference output data ' + str(test) + ' saved')



    # Generate Testing data
    print('\n')
    print('Generating testing data ' + str(test))
    SDRs, tags = SOM.inference('Testing_Data' + str(test), randomness, sparsity)

    print('Saving testing output ' + str(test))
    
    data = {'SDRs': SDRs,\
            'tags': tags}
    
    fileName = 'Testing_Output_Data'
    sio.savemat('./' + fileName + str(test), {'data': data})
    print('Testing output data ' + str(test) + ' saved')
