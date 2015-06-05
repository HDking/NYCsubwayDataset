from pandas import DataFrame, Series
import numpy

#################
# Syntax Reminder:
#
# The following code would create a two-column pandas DataFrame
# named df with columns labeled 'name' and 'age':
#
# people = ['Sarah', 'Mike', 'Chrisna']
# ages  =  [28, 32, 25]
# df = DataFrame({'name' : Series(people),
#                 'age'  : Series(ages)})

#function which creates a dataframe
def create_dataframe():
	countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympic_medal_counts = {
    	'country_name' : Series(countries),
    	'gold': Series(gold),
    	'silver': Series(silver),
    	'bronze': Series(bronze)
    	}
    df = DataFrame(olympic_medal_counts)

#function which computes the average number of bronze medals earned by countries who earned at least one gold medal.
avg_bronze_at_least_one_gold = numpy.mean(df['bronze'][df['gold']>=1])
#gives the means of the gold, silver and bronze medals
avg_medal_count = df[['gold','silver','bronze']].apply(numpy.mean)
#a function that returns the points by multiplying with numpy.dot
pgold = numpy.dot(gold,4)
    psilver = numpy.dot(silver,2)
    pbronze = numpy.dot(bronze,1)
    points = pgold + psilver + pbronze
    olympic_points ={
        'country_name': Series(countries),
        'points': Series(points)
    }
    df = DataFrame(olympic_points)
    return df

#refactored:
df['points'] = df[['gold','silver','bronze']].dot([4, 2, 1])
olympic_points_df = df[['country_name','points']]

#accessing more than one column - list of columns 
df[['country_name','age']]
#accessing certain rows - with index a
df.loc['a']
#select columns with selectors
df[df['age'] >= 30]
#To get a subset from a subset. Expl: the first gives only the survived column and the second stating ONLY from a set specified
df['survived?'][df['age']>=30]
#ask for the mean for every single column. This returns the mean for every column
df.apply(numpy.mean)
#You can also apply operations per datapoint
df['one'].map(lambda x: x>= 1) #will check if the numbers are equal or higher than one and returns TRUE or False (in the specified column)
df.applymap(lambda x: x>= 1) # will do the same as the above but then for the entire dataframe
#dot product between two vectors
numpy.dot(a,b) #this can also work for matrices with different sizes