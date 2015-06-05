import  numpy as np 
import pandas
from sklearn.linear_model import SGDRegressor

def normalize_featues(features):
	means = np.mean(features, axis=0)
	std_dev = np.std(features, axis=0)
	normalized_features = (features-means)/std_devs
	return means, std_devs, normalized_features

def recover_params(means, std_devs, norm_intercept,norm_params):
	intercept = norm_intercept - np.sum(means * norm_params / std_devs)
	params = norm_params / std_devs
	return intercept, params

def linear_regression(features, values):

	return intercept, params

def predictions(dataframe):
	#Select Features 
	features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]

	# Add UNIT to features using dummy variables
	dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
	features = features.join(dummy_units)

	#values
	values = dataframe['ENTRIESn_hourly']

	#Get the numpy arrays
	features_array = features.values
	values_array = values.values

	means, std_devs, normalized_features_array = normalized_features(features_array)

	#Perform gradient descent
	norm_intercept, norm_params = linear_regression(normalized_features_array, values_array)

	intercept, params = recover_params(means, std_devs, norm_intercept, norm_params)

	predictions = intercept + np.dot(features_array, params)

	return predictions