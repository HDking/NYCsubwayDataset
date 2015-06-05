import numpy as np
import pandas
import statsmodels.api as sm

dataframe = pandas.read_csv('/home/hao/Desktop/dataScience/introDS/turnstile_data_master_with_weather.csv', index_col=0)
#dataframe = pandas.DataFrame(data, columns = ['UNIT', 'DATEn', 'Hour', 'DESCn', 'ENTRIESn_hourly', 'EXITSn_hourly', 'maxpressurei', 'maxdewpti', 'mindewpti','minpressurei', 'meandewpti','meanpressurei', 'fog','rain','meanwindspdi','mintempi','meantempi','maxtempi', 'precipi','thunder'])

def linear_regression(features,values):
	Y = values
	X = features
	X = sm.add_constant(X)

	model = sm.OLS(Y,X)
	results = model.fit()
	#The intercept returns as the first value 
	intercept, params = results.params[0], (results.params[1:])
	return intercept, params

def predictions(dataframe):

	# select features (try different features!)
	features = dataframe[['Hour']]
 
	#Add UNIT to features using dummy variables
	dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
	features = features.join(dummy_units)

	#values
	values = dataframe['ENTRIESn_hourly']																																																											

	#Get the numpy arrays 
	features_array = features.values
	values_array = values.values

	#Perform lineair linear_regression
	intercept, params = linear_regression(features_array, values_array)					

	predictions = intercept + np.dot(features_array, params)
	return predictions
	
def compute_r_squared(data, predictions):
    boven = np.square(data-predictions)																																						
    sumBoven = np.sum(boven)
	onder = np.square(data-np.meantempi(data))
    sumOnder = np.sum(onder)
    																																																																																																																																																																				
    divide = sumBoven/sumOnder
    r_squared  =  1 - divide													
    #return r_squared
    return r_squared

predictions(dataframe)