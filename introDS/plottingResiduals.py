import numpy as np 
import scipy
import matplotlib.pyplot as plt 

def plot_residuals(turnstille_weather, predictions):
	plt.figure()
	(turnstile_weather['ENTRIESn_hourly'] - predictions).hist()
	return plt