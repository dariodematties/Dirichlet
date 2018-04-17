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

# File Name:		ravelMultiIndex.m
# Language:		GNU Octave high-level interpreted language.

# This function generates random samples from the Dirichlet process through the Chinese restaurant method.
# Those random samples are probability mass functions (pmf).

# Inputs:
#	coordinatesOfArray:			These are the coordinates of the element in the array from which we want its flat position index.
#	dimensionsOfArray:			These are the dimensions of the array.

# Outputs:
#	index:					This is the flat position index of the element in the array.

# Examples:
#
#	octave:2> ravelMultiIndex([2,0],[3,5])
#	ans =  10

function index = ravelMultiIndex(coordinatesOfArray, dimensionsOfArray)

	if length(coordinatesOfArray) != length(dimensionsOfArray)
		error("the two input arrays have different number of elements\n")
	endif

	for i = 1:length(coordinatesOfArray)
		if coordinatesOfArray(i) >= dimensionsOfArray(i)
			string = ["Coordinate " num2str(i) " overflow its dimension\n"];
			error(string)
		endif
	endfor

	numberOfCoordinates = length(dimensionsOfArray);

	if numberOfCoordinates == 1
		index = coordinatesOfArray;
	else
		index = 0;
		for i = 1:numberOfCoordinates
			if dimensionsOfArray(i) <= 0 || coordinatesOfArray(i) < 0
				error("at least one array dimension or array coordinate is <= 0\n")
			endif

			product = 1;
			if i < numberOfCoordinates
				for j = 2+(i-1):numberOfCoordinates
					product *= dimensionsOfArray(j);
				endfor
			endif

			index += product*coordinatesOfArray(i);
		endfor
	endif
endfunction
