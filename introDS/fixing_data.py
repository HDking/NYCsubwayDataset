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