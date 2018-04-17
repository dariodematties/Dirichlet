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

# File Name:		unravelIndex.m
# Language:		GNU Octave high-level interpreted language.

# This function generates random samples from the Dirichlet process through the Chinese restaurant method.
# Those random samples are probability mass functions (pmf).

# Inputs:
#	Index:			This is the flat position index of the element in the array.
#	dimensionsOfArray:	These are the dimensions of the array.

# Outputs:
#	coordinates:		These are the coordinates of the element in the array from which we want its flat position index.

# Examples:
#
#	octave:1> unravelIndex(8,[3,5])
#	ans =

#	   1   3

function coordinates = unravelIndex(Index, dimensionsOfArray)

	numberOfCoordinates = length(dimensionsOfArray);

	if Index >= prod(dimensionsOfArray)
		error("Index is bigger than the number of elements in the array\n")
	endif

	if numberOfCoordinates == 1
		coordinates = Index;
	else
		aux = Index;
		for i = numberOfCoordinates:-1:1
			if dimensionsOfArray(i) <= 0
				error("at least one array coordinate is <= 0\n")
			endif
			coordinates(i) = mod(aux,dimensionsOfArray(i));
			aux = floor(aux/dimensionsOfArray(i));
		endfor
	endif
endfunction
