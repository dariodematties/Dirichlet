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

# File Name:		Stick_breaking_Dir_dist_function.m
# Language:		GNU Octave high-level interpreted language.

# This function generates random samples from the Dirichlet distribution through the Stick-breaking method. Those random samples are probability mass functions (pmf).

# Inputs:
#	alpha:		Parameter of the Dirichlet distribution Dir(alpha). This parameter is a column vector of k components.

# Outputs:
#	Q_vector:	A k components vector which is a pmf.

function Q_vector = Stick_breaking_Dir_dist_function(alpha)

# checks the function arguments
if (nargin != 1)
	usage ("Stick_breaking_Dir_dist_function (alpha)");
endif

[k, a]=size(alpha);					# Extracts the number of components from the parameter vector alpha and put it in k.

if (a!=1)
	error("alpha must be a column vector with a dimensionality (k,1)")
endif

if (any(alpha<=0))
	error("alpha components must be >0")
endif

alpha=alpha';						# tramposes alpha and transforms it into a row vector
alpha_sum=flip(cumsum(flip(alpha(1,2:end))));		# accumulates alpha's components i.e. alpha=[1,2,3,4,5] then alpha_sum=[14,12,9,5]
u=betarnd(alpha(1,1:end-1),alpha_sum);			# generates samples from beta dist [u1 u2 u3 u4]=betarnd([1,2,3,4],[14,12,9,5])
remainder=cumprod(1-u);					# computes the stick remainders [(1-u1) (1-u1)(1-u2) (1-u1)(1-u2)(1-u3) (1-u1)(1-u2)(1-u3)(1-u4)]
Q_vector=[u 1].*[1 remainder];				# element wise mult [1*u1 (1-u1)*u2 (1-u1)(1-u2)*u3 (1-u1)(1-u2)(1-u3)*u4 (1-u1)(1-u2)(1-u3)(1-u4)*1]

endfunction
