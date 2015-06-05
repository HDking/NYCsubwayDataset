import numpy as np 
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
	#turnstile_weather is een data frame
	# Je wilt de gemiddelden hebben en 
	without_rain_mean = np.mean(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==0])
	with_rain_mean = np.mean(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==1])


	#de Mann Whittney Y test op ENTRIESn_hourly doen
	test = scipy.stats.mannwhitneyu(with_rain_mean, without_rain_mean, use_continuity=TRUE)
	U = test[1]
	p = test[2]
	return with_rain_mean, without_rain_mean, U, p

	#teruggeven: 
	# het gemiddelde van de regen entries 
	# het gemiddelde van entries zonder regen
	#de Mann-whitney U statistic en p-value comparing the number of entries with rain and the number of entries without rain



	#mannwhitneyu: 
	#scipy.stats.mannwhitneyu(x,y,use_continuity=TRUE)