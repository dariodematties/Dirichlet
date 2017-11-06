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

# File Name:		Chinese_restaurant_process.m
# Language:		GNU Octave high-level interpreted language.

# This function generates random samples from the Dirichlet process through the Chinese restaurant method.
# Those random samples are probability mass functions (pmf).

# Inputs:
#	num_customers:			This is the number of customers to which assign tables.
#	alpha:				Dispersion parameter of the Dirichlet process. This parameter is a scalar.

# Outputs:
#	table_assignments:	A vector with the table assignments in the restaurante.

# Examples:
#
#	Chinese_restaurant_process(10,1)
#
#	1   2   3   4   1   3   4   3   1   1


function table_assignments = Chinese_restaurant_process(num_customers, alpha)

# checks the function arguments
if (nargin != 2)
	usage ("Chinese_restaurant_process(num_customers, alpha)");
endif

if (!isscalar(alpha) || alpha<=0)
	error("alpha must be a scalar and it must be >0")
endif

if (mod(num_customers,1) != 0 || num_customers <= 0 || !isscalar(num_customers))
	error("num_customers must be a scalar natural value >0")
endif

table_assignments = [1];	# first customer sits at table 1
next_open_table = 2;		# index of the next empty table
# generates the table assignments for the rest of the customers.
for i = 2:num_customers
	if (rand < alpha/(alpha + i))
		# a new customer sits at a new table.
		table_assignments = [table_assignments next_open_table];
		next_open_table += 1;
	else
		# a new customer sits at an existing table.
		# this customer chooses which table to sit at by giving equal weight to each
		# customer already sitting at a table. 
		which_table = table_assignments(randi(length(table_assignments)));
		table_assignments = [table_assignments which_table];
	end
end

endfunction
