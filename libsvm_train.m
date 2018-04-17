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

# File Name:		libsvm_train.m
# Language:		GNU Octave high-level interpreted language.

function libsvm_train(kernel_type)

if ( nargin ~= 1 )
	error('Bad number of input arguments')
endif

if ( kernel_type ~= 0 && kernel_type ~= 2 )
	error('Bad kernel type')
endif

# load the files needed to feed libsvm
i=0;
string = ['Inference_Data' num2str(i)];
string = [string '.mat'];
string1 = ['Inference_Output_Data' num2str(i)];
string1 = [string1 '.mat'];
samples_av_model = 0;
clustering_av_model = 0;
while (exist (string) && exist (string1))

	load (string)
	
	disp(['Training libsvm with data from file ' string])
	disp("\n")

	training_label_vector = double(data.labels');
	if ( kernel_type == 2 )
		options = '-t 2 -v 5 -q';
	else
		options = '-t 0 -v 5 -q';
	endif

	# train libsvm for Inference_Data
	best_model = 0;
	best_cost = 1;
	training_instance_matrix = double(data.samples);

	if ( kernel_type == 2 )
		% coarse training
		for c = -5:15
			for g = -15:3
				libsvm_options = [options ' -c ' num2str(2^c) ' -g ' num2str(2^g)];
				cd ~/Downloads/libsvm-3.22/matlab
				model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
				cd ~/Contenidos/Tomasello/Dirichlet/Software
				if (model > best_model)
					best_model = model;
					best_cost = c;
					best_gamma = g;
				end
			end
		end
		% fine-grained training
		costs = [best_cost-1:0.1:best_cost+1];
		gammas = [best_gamma-1:0.1:best_gamma+1];
		for c = costs
			for g = gammas
				libsvm_options = [options ' -c ' num2str(2^c) ' -g ' num2str(2^g)];
				cd ~/Downloads/libsvm-3.22/matlab
				model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
				cd ~/Contenidos/Tomasello/Dirichlet/Software
				if (model > best_model)
					best_model = model;
					best_cost = c;
					best_gamma = g;
				end
			end
		end
		disp('The best model for inputs gives Accuracy = ');
		disp(best_model);
		training_options = ['-t 2 -q -c ' num2str(2^best_cost) ' -g ' num2str(2^best_gamma)];
		best_model = svmtrain(training_label_vector, training_instance_matrix, [training_options]);
	else
		# coarse training
		for c = -5:15
			libsvm_options = [options " -c " num2str(2^c)];
			cd ~/Downloads/libsvm-3.22/matlab
			model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
			cd ~/Contenidos/Tomasello/Dirichlet/Software
			if (model > best_model)
				best_model = model;
				best_cost = c;
			endif
		endfor
		# fine-grained training
		costs = [best_cost-1:0.1:best_cost+1];
		for c = costs
			libsvm_options = [options " -c " num2str(2^c)];
			cd ~/Downloads/libsvm-3.22/matlab
			model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
			cd ~/Contenidos/Tomasello/Dirichlet/Software
			if (model > best_model)
				best_model = model;
				best_cost = c;
			endif
		endfor
		disp("The best model for inputs gives Accuracy = ");
		disp(best_model);
		samples_av_model += best_model;
		training_options = ['-t 0 -q -c ' num2str(2^best_cost)];
		cd ~/Downloads/libsvm-3.22/matlab
		best_model = svmtrain(training_label_vector, training_instance_matrix, [training_options]);
		cd ~/Contenidos/Tomasello/Dirichlet/Software
	endif

	# Saves the SVM model
	fileName = ['SVM_Model' num2str(i) '.mat'];
	save(fileName, 'best_model', 'best_cost')







	load (string1)
	
	disp("\n")
	disp(['Training libsvm with data from file ' string1])
	disp("\n")
	disp(['The sparsity of the data is: ' num2str(1.0 - (sum(sum(data.SDRs)/prod(size(data.SDRs)))))])
	disp("\n")

	training_label_vector = double(data.tags');
	if ( kernel_type == 2 )
		options = '-t 2 -v 5 -q';
	else
		options = '-t 0 -v 5 -q';
	endif

	# train libsvm for Inference_Output_Data
	best_model = 0;
	best_cost = 1;
	training_instance_matrix = double(data.SDRs);

	if ( kernel_type == 2 )
		% coarse training
		for c = -5:15
			for g = -15:3
				libsvm_options = [options ' -c ' num2str(2^c) ' -g ' num2str(2^g)];
				cd ~/Downloads/libsvm-3.22/matlab
				model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
				cd ~/Contenidos/Tomasello/Dirichlet/Software
				if (model > best_model)
					best_model = model;
					best_cost = c;
					best_gamma = g;
				end
			end
		end
		% fine-grained training
		costs = [best_cost-1:0.1:best_cost+1];
		gammas = [best_gamma-1:0.1:best_gamma+1];
		for c = costs
			for g = gammas
				libsvm_options = [options ' -c ' num2str(2^c) ' -g ' num2str(2^g)];
				cd ~/Downloads/libsvm-3.22/matlab
				model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
				cd ~/Contenidos/Tomasello/Dirichlet/Software
				if (model > best_model)
					best_model = model;
					best_cost = c;
					best_gamma = g;
				end
			end
		end
		disp('The best model for inputs gives Accuracy = ');
		disp(best_model);
		cd ~/Downloads/libsvm-3.22/matlab
		training_options = ['-t 2 -q -c ' num2str(2^best_cost) ' -g ' num2str(2^best_gamma)];
		best_model = svmtrain(training_label_vector, training_instance_matrix, [training_options]);
		cd ~/Contenidos/Tomasello/Dirichlet/Software
	else
		# coarse training
		for c = -5:15
			libsvm_options = [options " -c " num2str(2^c)];
			cd ~/Downloads/libsvm-3.22/matlab
			model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
			cd ~/Contenidos/Tomasello/Dirichlet/Software
			if (model > best_model)
				best_model = model;
				best_cost = c;
			endif
		endfor
		# fine-grained training
		costs = [best_cost-1:0.1:best_cost+1];
		for c = costs
			libsvm_options = [options " -c " num2str(2^c)];
			cd ~/Downloads/libsvm-3.22/matlab
			model = svmtrain(training_label_vector, training_instance_matrix, [libsvm_options]);
			cd ~/Contenidos/Tomasello/Dirichlet/Software
			if (model > best_model)
				best_model = model;
				best_cost = c;
			endif
		endfor
		disp("The best model for inputs gives Accuracy = ");
		disp(best_model);
		clustering_av_model += best_model;
		training_options = ['-t 0 -q -c ' num2str(2^best_cost)];
		cd ~/Downloads/libsvm-3.22/matlab
		best_model = svmtrain(training_label_vector, training_instance_matrix, [training_options]);
		cd ~/Contenidos/Tomasello/Dirichlet/Software
	endif

	# Saves the SVM model
	fileName = ['Clustering_SVM_Model' num2str(i) '.mat'];
	save(fileName, 'best_model', 'best_cost')


	i = i+1;
	string = ['Inference_Data' num2str(i)];
	string = [string '.mat'];
	string1 = ['Inference_Output_Data' num2str(i)];
	string1 = [string1 '.mat'];
endwhile



disp('Average training from samples is')
samples_av_model/i 

disp('Clustering average training is')
clustering_av_model/i 


endfunction
