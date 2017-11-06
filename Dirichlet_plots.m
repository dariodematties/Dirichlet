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

# File Name:		Dirichlet_plots.m
# Language:		GNU Octave high-level interpreted language.

# This function plots Beta and Dirichlet (for 3 dimensions) distributions with alpha parameter.

#Inputs:
#	alpha:		Parameter of the Dirichlet distribution Dir(alpha). This parameter is a row vector of 3 components.

#Outputs:
#	no return value.

# Examples:
#
#	Dirichlet_plots([10 10 10])
#
#	Dirichlet_plots([2 5 25])
#
#	Dirichlet_plots([0.2 0.2 0.2])


function	Dirichlet_plots(alpha)

# checks the function arguments
if (nargin != 1)
	usage ("Dirichlet_plots (alpha)");
endif

if (size(alpha)(1,1)!=1 || size(alpha)(1,2)!=3)
	if (size(alpha)(1,1)==3 || size(alpha)(1,2)!=1) 			# if alpha is a column vector, then
		alpha=alpha';							# transpose alpha
	else 									# if not, then there must be some error in the argument passed to the function
		error ("alpha argument must have dimensionality (1,3)");
	endif
endif

# constructs the simplex
x1=linspace(0,1,1000);
x2=linspace(0,1,1000);

[X1,X2]=ndgrid(x1,x2);
X3=1-X1-X2;

bad=(X1+X2>=1);

X1(bad)=NaN;
X2(bad)=NaN;
X3(bad)=NaN;

# computes the distributions
# computes the Beta distribution
Beta_distrib=(x1.^(alpha(1)-1).*(1-x1).^(alpha(2)-1))/beta(alpha(1),alpha(2));

# computes the Dirichlet distribution
Beta = exp(sum(gammaln(alpha))-gammaln(sum(alpha)));
Dirichlet_distrib=(X1.^(alpha(1)-1).*X2.^(alpha(2)-1).*X3.^(alpha(3)-1))/Beta;


# plots Beta distribution
figure, 

plot3(x1,1-x1,0*x1,x1,1-x1,Beta_distrib);
xlabel('x1');
ylabel('x2');
zlabel('Beta distrib');
view(169,50);

# plots Dirichlet distribution
figure,

surf(X1,X2,X3,Dirichlet_distrib,'EdgeColor','none');
title ('Dirichlet distrib');
xlabel('x1');
ylabel('x2');
zlabel('func(x1,x2,1-x1-x2)');
view(169,50);

# just if any(alpha<1), this is for visualization matterns
if (any(alpha<=1))
	caxis([0.2 4])
endif

colormap(jet)

endfunction
