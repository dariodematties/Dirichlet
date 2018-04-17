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

# File Name:		DrawLattice.m
# Language:		GNU Octave high-level interpreted language.

#This function draws the lattice.

function DrawLattice(weights, dimensionsOfArray)

	hold on;
	for i = 0:rows(weights)-2
		for j = i+1:rows(weights)-1
			coordinates1 = unravelIndex(i, dimensionsOfArray);
			coordinates2 = unravelIndex(j, dimensionsOfArray);
			distance = sum(abs(coordinates1-coordinates2));
			if (distance == 1)
				index1 = i+1;
				index2 = j+1;
				if (columns(weights) == 2)
					plot([weights(index1,1) weights(index2,1)],[weights(index1,2) weights(index2,2)],'b');
				elseif (columns(weights) == 3)
					plot3([weights(index1,1) weights(index2,1)],[weights(index1,2) weights(index2,2)],[weights(index1,3) weights(index2,3)],'b');
				else
					error("inputDimensionality exceeds the plots' possibilities.")
				endif
			endif
		endfor
	endfor
	hold off;

endfunction
