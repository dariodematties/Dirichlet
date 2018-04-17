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

# File Name:		libsvm_test.m
# Language:		GNU Octave high-level interpreted language.

function libsvm_test()

Average_Accuracy = 0;
Average_Clustering_Accuracy = 0;

# load the files needed to feed libsvm
i=0;
string = ['Testing_Data' num2str(i)];
string = [string '.mat'];
string1 = ['Testing_Output_Data' num2str(i)];
string1 = [string1 '.mat'];
while (exist (string) && exist (string1))

	load (string)
	
	disp(['Testing libsvm with data from file ' string])
	disp("\n")

	testing_instance_matrix = double(data.samples);
	testing_label_vector = double(data.labels');
	libsvm_options = '';

        # test libsvm for Testing_Data
        load(['SVM_Model' num2str(i) '.mat'])

        model = best_model;

	cd ~/Downloads/libsvm-3.22/matlab
	[predicted_label, accuracy, prob_estimates] = svmpredict(testing_label_vector, testing_instance_matrix, model, [libsvm_options]);
	cd ~/Contenidos/Tomasello/Dirichlet/Software
	disp(['For the SVM_Model' num2str(i) 'inputs to the model we have:']);
	disp("accuracy");
	disp(accuracy);
	Average_Accuracy += accuracy(1);
	save(['SVM_Model_Performance' num2str(i) '.mat'], 'predicted_label', 'accuracy', 'prob_estimates')


	load (string1)
	
	disp(['Testing libsvm with data from file ' string1])
	disp("\n")

	testing_instance_matrix = double(data.SDRs);
	testing_label_vector = double(data.tags');
	libsvm_options = '';

        # test libsvm for Testing_Data
        load(['Clustering_SVM_Model' num2str(i) '.mat'])

        model = best_model;

	cd ~/Downloads/libsvm-3.22/matlab
	[predicted_label, accuracy, prob_estimates] = svmpredict(testing_label_vector, testing_instance_matrix, model, [libsvm_options]);
	cd ~/Contenidos/Tomasello/Dirichlet/Software
	disp(['For the Clustering_SVM_Model' num2str(i) 'inputs to the model we have:']);
	disp("accuracy");
	disp(accuracy);
	Average_Clustering_Accuracy += accuracy(1);
	save(['Clustering_SVM_Model_Performance' num2str(i) '.mat'], 'predicted_label', 'accuracy', 'prob_estimates')


	i = i+1;
	string = ['Testing_Data' num2str(i)];
	string = [string '.mat'];
	string1 = ['Testing_Output_Data' num2str(i)];
	string1 = [string1 '.mat'];
endwhile

disp('Average Accuracy in the input is: ')
Average_Accuracy/i
disp('Average Clustering Accuracy in the input is: ')
Average_Clustering_Accuracy/i
endfunction
