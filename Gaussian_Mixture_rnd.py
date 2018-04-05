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

# File Name:		Gaussian_Mixture_rnd.py
# Language:		Python general-purpose interpreted high-level programming language.

# This function generates random samples from a multivariate mix of Gaussians.
# First: Sample I from categorical distribution parametrized by vector w=(w1,…,wd), such that wi≥0 and ∑i(wi)=1.
# Finally: Sample x from normal distribution parametrized by μI and σI.

# Inputs:
#	n:				An integer which specifies the number of samples to be generated from the
#					multivariate mixture of Gaussians.
#	w:				This is the vector of weights in order to choose the distribution.
#					w.shape
#					(d,)
#	mean:				An array with a row vector per mean for a Gaussian.
#					mean.shape
#					(d,f)
#					f is the number of features in each Gaussian.
#	cov:				An array with the covariance matrices.
#					cov.shape
#					(d,f,f)

# Outputs:
#	samples:			An array with the samples from the multivariate mix of Gaussians.
#					samples.shape
#					(n,f)

# Examples:
#
#	Stick_breaking_process(10,1)
#
#	1   2   3   4   1   3   4   3   1   1

import numpy as np

def Gaussian_Mixture_rnd(n, w, mean, cov):
    if (type(n) is not int) or \
       (type(w) is not np.ndarray) or \
       (type(mean) is not np.ndarray) or \
       (type(cov) is not np.ndarray) :
        print("In function Generate_Training_Data: n is not int or "\
              "w is not numpy array or "\
              "mean is not numpy array or "\
              "cov is not numpy array")
        raise ValueError('Generate_Training_Data error')
    
    if (len(w.shape) is not 1) or \
       (len(mean.shape) is not 2) or \
       (len(cov.shape) is not 3) or \
       (w.shape[0] is not mean.shape[0]) or \
       (mean.shape[0] is not cov.shape[0]) or \
       (mean.shape[1] is not cov.shape[1]) or \
       (mean.shape[1] is not cov.shape[2]) or \
       (mean.shape[0] is 0) or \
       (mean.shape[1] is 0) :
        print("In function Generate_Training_Data:"\
              "w has not a correct shape or "\
              "mean has not a correct shape or "\
              "cov has not a correct shape")
        raise ValueError('Generate_Training_Data error')

    I = np.array(range(w.size))
    choices = np.random.choice(I, n, p=w)
    uniques, counts = np.unique(choices, return_counts=True)
    a = dict(zip(uniques, counts))

    for unique in uniques :
        if unique == uniques[0]:
            samples = np.random.multivariate_normal(mean[unique], cov[unique], a[unique])
            labels = np.full((1,a[unique]),unique)
        else:
            samples = np.append(samples, np.random.multivariate_normal(mean[unique], cov[unique], a[unique]), axis=0)
            labels = np.append(labels,np.full((1,a[unique]),unique))

    labels = np.reshape(labels, (labels.size,1))
    samples = np.append(samples,labels,axis=1)
    np.random.shuffle(samples)

    return samples[0:n,0:mean.shape[1]], samples[0:n,mean.shape[1]].astype(int)


