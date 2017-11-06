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

# File Name:		Polya_urn_Dir_proc_function.m
# Language:		GNU Octave high-level interpreted language.

# This function generates random samples from the Dirichlet process through the Pólya's urn method. Those random samples are probability mass functions (pmf).

# Inputs:
#	base_color_distribution:	This is a function handle. This must be a color distribution to sample new colors.
#	num_balls:			This is the number of balls tu put in the urn.
#	alpha:				Dispersion parameter of the Dirichlet process. This parameter is a scalar.

# Outputs:
#	balls_in_urn:	A vector with the balls in the urn.

# Examples:
#
#	random_color = @() randi(100)/100;
#	Polya_urn_Dir_proc_function(random_color,10,1)
#
#	0.56000   0.56000   0.66000   0.88000   0.88000   0.66000   0.55000   0.66000   0.88000   0.66000


function balls_in_urn = Polya_urn_Dir_proc_function(base_color_distribution, num_balls, alpha)

# checks the function arguments
if (nargin != 3)
	usage ("Polya_urn_Dir_proc_function(base_color_distribution, num_balls, alpha)");
endif

if (!isscalar(alpha) || alpha<=0)
	error("alpha must be a scalar and it must be >0")
endif

if (mod(num_balls,1) != 0 || num_balls <= 0 || !isscalar(num_balls))
	error("num_balls must be a scalar natural value >0")
endif

if (!is_function_handle(base_color_distribution))
	error("base_color_distribution must be a function handle")
endif

balls_in_urn = [];		# this array represents the unr in which the balls are
for i = 1:num_balls
	if (rand < alpha/(alpha+length(balls_in_urn)))
		# draws a new color, puts a ball of this color in the urn
		new_color = base_color_distribution();
		balls_in_urn = [balls_in_urn new_color];
	else
		# draws a ball from the urn, add another ball of the same color
		ball = balls_in_urn(randi(length(balls_in_urn)));
		balls_in_urn = [balls_in_urn ball];
	endif
endfor

endfunction
