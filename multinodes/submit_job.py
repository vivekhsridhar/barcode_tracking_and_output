#!/usr/bin/env python
import csv, subprocess

'''Here you define where to look for the parameters file
where fileIDs are taken from'''
parameter_file_full_path='/beegfs/work/vsridhar/barcode_tracking/videos/files1.csv'

#Define output path
outpath = '/beegfs/work/vsridhar/barcode_tracking/output/leadership/day1_fish22'
#ifile  = open('sample.csv', "rt", encoding=<theencodingofthefile>)
with open(parameter_file_full_path,'rt', encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile)
	for fid in reader: 
		qsub_command = """qsub -v fid={0} -q long -l nodes=1:ppn=4 $HOME/multinodes2/job.sh""".format(*fid)
		print(qsub_command)

        	# Comment the following 3 lines when testing to prevent jobs from being submitted
		exit_status = subprocess.call(qsub_command, shell=True)
		if exit_status == 1:  # Check to make sure the job submitted
			print('fid {0} failed to submit'.format(qsub_command))
		
	
print('Done submitting jobs!')
