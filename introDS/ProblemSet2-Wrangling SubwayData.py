#problem 5
import csv

input_file = '/home/hao/Desktop/dataScience/introDS/input.txt'
output_file= '/home/hao/Desktop/dataScience/introDS/output.txt'

def fix_turnstile_data(filenames):
	for name in filenames:
	        f_in = open(name,"r")
	        f_out = open("updated_"+name,"w")

	        reader_in = csv.reader(f_in, delimiter=',')
	        writer_out = csv.writer(f_out, delimiter=',')

	        for line in reader_in:
	            offset = 3
	            for i in range(1,9):
	                if(len(line) >= (offset + 4)):
	                    line_out = [
	                        line[0], 
	                        line[1], 
	                        line[2], 
	                        line[offset],
	                        line[offset+1],
	                        line[offset+2],
	                        line[offset+3],
	                        line[offset+4]
	                        ]
	                    writer_out.writerow(line_out)
	                    offset = offset+5
	        f_in.close()
	        f_out.close()

#Problem 6
def create_master_turnstile_file(filenames, output_file):
	#'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn' These columns need to be included
	   with open(output_file, 'w') as master_file:
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       for filename in filenames:
            f_in = open(filename, 'r')
            for line in f_in:
                master_file.write(line)


Let op! Het kan dus ook zonder de import CSV..! 

#Problem 7
turnstile_data = pandas.DataFrame(pandas.read_csv(filename), columns=['C/A','UNIT','SCP','DATEn','TIMEn','DESCn','ENTRIESn','EXITSn'])
    # more of your code here
    turnstile_data = turnstile_data.loc[turnstile_data['DESCn'] == 'REGULAR']
    
    return turnstile_data

#Problem 10
    
    hour = int(time[0:2])
    
    return hour

#problem 8, 9 and 11 still open

