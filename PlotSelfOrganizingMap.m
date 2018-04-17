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

# File Name:		PlotSelfOrganizingMapPy.m
# Language:		GNU Octave high-level interpreted language.

#This program tests the Self Organizing Map plotting the units' lattice.

load SOM_Status.mat

if (status.SSOM1_inputDimensionality == 1)
	plot(1:length(status.SSOM1_weights),status.SSOM1_weights,'-o');
elseif (status.SSOM1_inputDimensionality == 2)
	scatter(status.SSOM1_weights(:,1),status.SSOM1_weights(:,2));
	DrawLattice(status.SSOM1_weights, double(status.SSOM1_unitsArrayDimensionality));
elseif (status.SSOM1_inputDimensionality == 3)
	scatter3(status.SSOM1_weights(:,1),status.SSOM1_weights(:,2),status.SSOM1_weights(:,3));
	DrawLattice(status.SSOM1_weights, double(status.SSOM1_unitsArrayDimensionality));
else
	error("inputDimensionality exceeds the plots' possibilities.")
endif
