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

# File Name:		Stick_breaking_process.m
# Language:		GNU Octave high-level interpreted language.

# This function generates random samples from the Dirichlet process through the stick breaking method.
# Those random samples are probability mass functions (pmf).

# Inputs:
#	num_weights:			This is the number of weightsl in which the stick is breaken.
#	alpha:				Dispersion parameter of the Dirichlet process. This parameter is a scalar.

# Outputs:
#	weights:			A vector with the stick weights  

# Examples:
#
#	Stick_breaking_process(10,1)
#
#	1   2   3   4   1   3   4   3   1   1


function weights = Stick_breaking_process(num_weights, alpha)

# checks the function arguments
if (nargin != 2)
	usage ("Stick_breaking_process(num_weights, alpha)");
endif

if (!isscalar(alpha) || alpha<=0)
	error("alpha must be a scalar and it must be >0")
endif

if (mod(num_weights,1) != 0 || num_weights <= 0 || !isscalar(num_weights))
	error("num_weights must be a scalar natural value >0")
endif

# computes a vector with all betas
betas = betarnd(1, alpha, 1, num_weights-1);

remaining_stick_lengths = cumprod(1-betas);
weights = [betas 1].*[1 remaining_stick_lengths];

endfunction
