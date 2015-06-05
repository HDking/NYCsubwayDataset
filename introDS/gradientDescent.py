import numpy
import pandas

def compute_cost(features,values,theta):
	"""
	Compute the cost of a list of parameters, given a list of features
	(input data points) and values (output data points)
	"""

	m = len(values)
	sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
	cost = sum_of_square_errors / (2*m)

	return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
	"""Perform gradient descent given a data set 
	with an arbritrary number of features"""
	#sowieso een for loop met num_iterations er in 
	m = len(values)
	cost_history = []

	for i in range(num_iterations):
		predicted_values = numpy.dot(features,theta)
		theta = theta - alpha / m * numpy.dot((predicted_values - values), features)

		cost = compute_cost(features, values, theta)
		cost_history.append(cost)

	# we have a starting point where J(theta) is large and we keep on updating 
	# theta's until we find that J(theta) is at its minimum. 
	# zie de tweede formule van het vorige filmpje (dat is hem uitgewerkt)
	# alpha is learning rate (small step)



## write code that performs num_iterations to the elements of theta times. 
## every time you compute the cost for a given list of thetas, append it to
## cost_history.

	cost_history = []


	return theta, pandas.Series(cost_history)