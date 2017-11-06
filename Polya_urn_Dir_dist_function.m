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

# File Name:		Polya_urn_Dir_dist_function.m
# Language:		GNU Octave high-level interpreted language.

# This function generates random samples from the Dirichlet distribution through the Pólya's urn method. Those random samples are probability mass functions (pmf).

# Inputs:
#	alpha:		Parameter of the Dirichlet distribution Dir(alpha). This parameter is a column vector of k components.
#	N_iterations:	Number of iterations to generate a random sample.

# Outputs:
#	Q_vector:	A k components vector which is a pmf.

function Q_vector = Polya_urn_Dir_dist_function(alpha, N_iterations)

# checks the function arguments
if (nargin != 2)
	usage ("Polya_urn_Dir_dist_function (alpha, N_iterations)");
endif

[k, a]=size(alpha);				# Extracts the number of components from the parameter vector alpha and put it in k.

if (a!=1)
	error("alpha must be a column vector with a dimensionality (k,1)")
endif

if (any(alpha<=0))
	error("alpha components must be >0")
endif

if (mod(N_iterations,1) != 0 || N_iterations <= 0 || !isscalar(N_iterations))
	error("N_iterations must be a scalar natural value >0")
endif

alpha_0=sum(alpha);				# Sums all the components of alpha.

p=alpha/alpha_0;				# Determines a pmf vector for use it in the multinomial distribution.

q=zeros(k,1);					# Prepares the output vector

for i=1:N_iterations

	x=mnrnd(1,p);				# Extracts a ball from the urn.

	q=q+x';					# Adds the color of the ball.

	alpha=alpha+x';				# Return the ball to the urn with another ball of the same color.

	alpha_0=sum(alpha);			# Sums all the components of alpha.

	p=alpha/alpha_0;			# Determines a pmf vector for use it in the multinomial distribution.

endfor


q_0=sum(q);					# Sums all the components of q.

Q_vector=q/q_0;					# Determines a pmf vector for use it in the multinomial distribution.


endfunction
