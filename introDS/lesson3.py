#how to do this in python
import scipy.stats
scipy.states.ttest_ind(list_1, list_2, equal_var=False)

#Welch's t-Test Exercise
import numpy
import scipy.stats
import pandas

# parametric test
def compare_averages(filename):
	#read the data into a pandas data frame
	#one dataframe is left-handed the other right-handed
	#alleen de lijsten waar de averages in staan. 

	#run Welch's t-test on the two cohorts defined by handedness
	scipy.stats.ttest_ind(left,right, equal_var=False)
	# We can use this test, if we observe two independent samples from the same or different population, e.g. exam scores of boys and girls or of two ethnic groups.
	#The test measures whether the average (expected) value differs significantly across samples. If we observe a large p-value, for example larger than 0.05 or 0.1, 
	# than we cannot reject the null hypothesis of identical average scores. If the p-value is smaller than the treshold e.g. 1%, 5% or 10%, then we reject the 
	#null hypothesis of equal averages. 
	#returns : (t, prob). prob is the two-tailed p-value

	#with a significance level of 95%, if there is no differencce: reeturn a tuple consisting of True, and then the tuple returned by scipy.stats.ttest
	#if there is a difference, return a typle consisting of False, and then the typle returned by scipy.stats.ttest. 

	df = pandas.DataFrame(pandas.read_csv(filename), columns = ['name', 'handedness', 'avg'])
    left = df['avg'][df['handedness'] == 'L']
    right = df['avg'][df['handedness'] == 'R']
    
    tTest = scipy.stats.ttest_ind(left,right,equal_var=False)
    t = tTest[0]
    p = tTest[1]
    crit = 0.95
    if p < (1-crit):
        return (False, (t, p))
    else:
        return (True,(t,p))

#Non-parametric test: Mann-Whitney u test - tests null hypothesis that two populations are the same
#Does not assume the data is drawn from any particulkar underlying probability distribution
u,p = scipy.stats.mannwhitneyu(sample1, sample2)
# --> did these two samples come from the same group

#non-normal data:
#Shapiro-Wilk Test: p is the same as the ttest
w,p = scipy.stats.shapiro(data)

 