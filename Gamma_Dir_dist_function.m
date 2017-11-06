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

# File Name:		Gamma_Dir_dist_function.m
# Language:		GNU Octave high-level interpreted language.


# This function generates random samples from the Dirichlet distribution through the generating random variables
# from the Gamma distribution. Those random samples are probability mass functions (pmf).

# Inputs:
#	alpha:		Parameter of the Dirichlet distribution Dir(alpha). This parameter is a column vector of k components.

# Outputs:
#	Q_vector:	A k components vector which is a pmf.

function Q_vector = Gamma_Dir_dist_function(alpha)

# checks the function arguments
if (nargin != 1)
	usage ("Gamma_Dir_dist_function (alpha)");
endif

[k, a]=size(alpha);				# Extracts the number of components from the parameter vector alpha and put it in k.

if (a!=1)
	error("alpha must be a column vector with a dimensionality (k,1)")
endif

if (any(alpha<=0))
	error("alpha components must be >0")
endif

z=gamrnd(alpha',1);				# Generates a k drawns from the Gamma distribution.

Q_vector=z/(sum(z));				# Returns the output vector.

endfunction
