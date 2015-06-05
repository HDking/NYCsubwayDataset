def create_master_turnstile_file(filenames, output_file):
	#'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn' These columns need to be included
	   with open(output_file, 'w') as master_file:
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       for filename in filenames:
            f_in = open(filename, 'r')
            for line in f_in:
                master_file.write(line)


Let op! Het kan dus ook zonder de import CSV..! 