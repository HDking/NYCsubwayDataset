#print ggplot(data, aes(xvar,yvar)) + geom_point(color = 'coral') + geom_line('coral') + ggtitle('title') + xlab('x-label') + ylab('y-label')
from pandas import * 
from ggplot import *

import pandas

def lineplot(hr_year_csv):
	dataframe = pandas.read_csv('/home/hao/Desktop/dataScience/introDS/lesson4/hr_year.csv')
	gg= ggplot(dataframe, aes(x='yearID',y= 'HR')) +  geom_point(color='red') + geom_line(color='red') + ggtitle('Total HRs by Year') + xlabel('Year') + ylabel('HR')
	return gg

lineplot(hr_year_csv)

def lineplot_compare(hr_by_team_year_sf_la_csv):
	#ggplot(data, aes(xvar, yvar, color=category_var))
	dataframe = pandas.read_csv(hr_by_team_year_sf_la_csv)
	gg = ggplot(dataframe, aes(x='yearID', y='HR', color='teamID'))

	#gives the plot with the two categories seperated from each other. 
	gg = ggplot(dataframe, aes(x='yearID', y='HR', color='teamID')) + geom_point() + geom_line()