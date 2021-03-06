#!/usr/bin/python3

import os
import sys
import re
from pytvdbapi import api

# Connect to The TVDB api
db = api.TVDB('F506627134A2D5E9')

# Save path and name of the file in two variables
folder = sys.argv[1]

fold = [d for d in os.listdir(folder)]

for each in fold:
	# Connect to The TVDB api
	db = api.TVDB('F506627134A2D5E9')
	file_name = each
	if sys.platform == 'win32':
		path = folder + '\\'+ file_name
	else:
		path = folder + '/' + file_name
	# Extracting Show name, Season and Episode Numbers
	file_name = file_name.lower()
	extension = file_name.split('.')[-1]

	restricted = ['avi','mkv','mp4', 
		'X264', 'DIMENSION', 'HDTV', 
		'DDLValley', 'eu', 'sdtv',
		'720p', '480p', 'LOL',
		'_', '-', 'compulsion',
		'xvid', 'ASAP', 'fqm',
		'[', ']', 'vtv', 'remarkable',
		'afg', 'proper', 'repack',
		'2hd', 'evolve', 'www',
		'tuserie', 'real', '300mblinks',
		'fever', 'theextopia', 
		'killers','publicHD', 'mrs',
		'com','net', 'patoghdl'
		]

	restricted = [each.lower() for each in restricted]

	for me in restricted:
		file_name = file_name.replace(me, " ")

	show_name = file_name.replace(".", " ")

	num = re.compile("[0-9]+")

	season = re.compile("s[0-9]+",flags=re.IGNORECASE)
	se = season.findall(show_name)[0]
	show_name = show_name.replace(se, '')
	se_string = num.findall(se)[0]
	#print(se, se_string)
	se = int(se_string)
	if se<10:
		se %= 10

	episode = re.compile("e[0-9]+", flags=re.IGNORECASE)
	ep = episode.findall(show_name)[0]
	show_name = show_name.split(ep)[0]
	ep_string = num.findall(ep)[0]
	ep = int(ep_string)
	if ep<10:
		ep %= 10

	show_name = show_name.lstrip()
	show_name = show_name.rstrip()
	show_name = show_name.title()

	# Getting the name of the episode
	result = db.search(show_name, "en")
	show = result[0]
	ep_title = show[se][ep].EpisodeName
	# Renaming the file
	new_name = show_name + ' - S' +se_string+'E'+ep_string+' - '+str(ep_title)+'.'+str(extension)
	if sys.platform == 'win32':
		new_path = path.replace(str(path.split('\\')[-1]),new_name)
	else:
		new_path = path.replace(str(path.split('/')[-1]),new_name)
	os.rename(each, new_name)
	print('The file has successfully been renamed to %s' % (new_name))
