#!/usr/bin/env python

import csv, subprocess
import os
import pwd
from pinpoint import Tracker, VideoReader


#import sys
#sys.path.append('$HOME/multijobs/site-packages')
#import timing


#userid = pwd.getpwuid( os.getuid() ).pw_name
blocksize = 19
offset = 6

#pinpoint_dict = '/beegfs/work/kn_pop512620/pinpoint/barcodes/3x3_2bit/master_list.pkl'
'''Read parameters file to give ID names'''
parameter_file_full_path='/beegfs/work/vsridhar/barcode_tracking/videos/files1.csv'
#ifile  = open('sample.csv', "rt", encoding=<theencodingofthefile>)
with open(parameter_file_full_path,'rt', encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile)
	for fileid in reader: 
		video_extension = 'mp4'
		videopath = '/beegfs/work/vsridhar/barcode_tracking/videos/'
		videoID = """{0}""".format(*fileid)
		outputname = videoID+'_tracks.h5'
		print(outputname)
		out_path = '/beegfs/work/vsridhar/barcode_tracking/output/leadership/day1_fish22'
		#Check if outputfolder already exists, create a new one otherwise
		#if not os.path.exists(out_path):
		#	os.makedirs(out_path)
		videofile = videopath+videoID+'.'+video_extension
		print(videofile)
		print(videoID)
		
		#logging_info(out_path,videoID,blocksize, offset)			
		'''Here's where tracking happens'''
		tracker = Tracker(source=videofile,
					block_size=blocksize,
					offset=offset,
					distance_threshold=20,
					area_range=(60,200),
					tolerance=0.1,
					channel='green',
					resize=2)

		tracker.load_dict('/beegfs/work/vsridhar/pinpoint/barcodes/3x3_2bit/master_list.pkl')
		#tracker.track(out_path+'/'+outputname, batch_size=200, n_jobs=-1)
		tracker.track(out_path+'/'+outputname, batch_size=200, n_jobs=-1)
