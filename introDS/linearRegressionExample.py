import statsmodels.api as sm 

def linear_regression(features, values):
	Y = values
	X = features
	X = sm.add_constant(X)

	model = sm.OLS(Y,X)
	results = model.fit()
	intercept, params = results.params[0], (results.params[1], results.params[2])

	