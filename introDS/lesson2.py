#This lesson is about Data Wrangling
import pandas
import pandasql
#To be able to read JSON formats
import json
import requests

#import a CSV file
baseball_data = pandas.read_csv('Master.csv')

print baseball_data['name_First']

#add to columns to each other
baseball_data['height-plus-weight'] = baseball_data['height'] + baseball_data['height']
baseball_data['nameFull'] = baseball_data['nameFirst'] + " " + baseball_data['nameLast']

#write to CSV file
baseball_data.to_csv('baseball_data_names.csv')

#SQL 
#Select all data from a certain table
SELECT * FROM [table] LIMIT 20;
SELECT * FROM aadhaar_data WHERE state='Gujarat';
SELECT district, SUM(adhaar_generated) FROM aadhar_data GROUP BY district;

#Rename the columns by replacing spaces with underscores and setting all characters to
#to lowercase, so the column names more closely resemble column names one might
# find in a table
aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

#Execute your SQL command against the pandas frame q is the SQL query 
aadhaar_solution = pandasql.sqldf(q.lower(), locals())

    # Write a query that will select from the aadhaar_data table how many men and how 
    # many women over the age of 50 have had aadhaar generated for them in each district
    #What is important is that everything that you do not have an aggregate function for, you need to group by
"select gender, district, sum(aadhaar_generated) from aadhaar_data where age>50 group by gender, district;"

#API: Application Programming Interface
Common ones: REST API 
if __name__  = "__main__":
	url = ''
	data = requests.get(url).text
	#turns JSON to a Python dictionary
	data = json.loads(data)
	print type(data)
	print data
	data['artist']

#Sanity checking (make sense? Is there are problem? Does the data look like I expect it is?)
#Pandas describe function
baseball = pandas.read_csv('')
baseball.describe()

#Dealing with missing data
- Partial deletion: 1) listwise deletion, 2) pairwise deletion
- Imputation: Give the missing data the mean values. But changes correlation. OR make a linear model that fills in the missing values. 

#fillna(value)
# call it like this: dataframe['column'] = dataframe['column'].fillna(value)
baseball = pandas.read_csv(filename)
    baseball['weight'] = baseball['weight'].fillna(numpy.mean(baseball['weight']))
    print numpy.sum(baseball['weight']), numpy.mean(baseball['weight'])

#return a value as an integer
cast(maxtempi as integer)
#foggy example
select fog, max(maxtempi) as maxtempi from weather_data group by fog;

#You can convert dates to days of the week via the 'strftime' keyword in SQL. 
#For example, cast (strtime('%w', date) as integer) will return 0 if the date is a Sunday or 6 if the date is a Saturday
cast(strftime('%w', date) as integer) 
select avg(cast (meantempi as integer)) from weather_data where cast(strftime('%w',date) as integer) == 0 or cast(strftime('%w', date) as integer) == 6;

#avg minimum temperature (mintempi) on rainy daus (rain = 1) where mintempi is greater than 55 degrees
select avg(cast(mintempi as integer)) from weather_data where rain==1 and mintempi > 55;

#You want to write a function that will update each row in the text file so there is only one entry per row. 
#Write the updates to a different text file in the format of "updated_" + filename. 
f_in = open('','r')
# the updated files go here
f_out = open('', 'w')

#creaer csv readers and writers based on our file objects
reader_in = csv.reader(f_in, delimiter=',')
reader_out = csv.reader(f_out, delimiter= ',')

#Skip the first line because it contains headers
reader_in.next()

#Our reader_in allows us to go through each line (row of the input data) and access its data with the standard Python syntax: 
for line in reader_in: 
	type_chocolate = line[0]
	#For each line, the format will be: 
	#type_choco, batch_id, cocoa, milk, sugar
	line_1 = [type_chocolate, line[1], line[2], line[3], line[4]]
	line_2 = [type_chocolate, line[5], line[6], line[7], line[8]]
	writer_out.writerow(line_1)
	writer_out.writerow(line_2)

#finally, we have to close both of our final objects!
f_in.close()
f_out.close()