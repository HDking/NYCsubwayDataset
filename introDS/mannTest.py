import numpy as np 
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
	#turnstile_weather is een data frame
	# Je wilt de gemiddelden hebben en 
	sample_with_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==1]
    sample_without_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==0]
    without_rain_mean = np.mean(sample_with_rain)
    with_rain_mean = np.mean(sample_without_rain)
    test = scipy.stats.mannwhitneyu(sample_with_rain, sample_without_rain, use_continuity=True)
    U = test[0]
    p = test[1]
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader

	#teruggeven: 
	# het gemiddelde van de regen entries 
	# het gemiddelde van entries zonder regen
	#de Mann-whitney U statistic en p-value comparing the number of entries with rain and the number of entries without rain



	#mannwhitneyu: 
	#scipy.stats.mannwhitneyu(x,y,use_continuity=TRUE)