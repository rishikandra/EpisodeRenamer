#!/usr/bin/python3

import os
import sys
import re
from pytvdbapi import api

# Connect to The TVDB api
db = api.TVDB('F506627134A2D5E9')

# Save path and name of the file in two variables
path = sys.argv[1]
if sys.platform == 'win32':
	file_name = path.split('\\')[-1]
else:
	file_name = path.split('/')[-1]

# Extracting Show name, extension, Season and Episode Numbers
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
	'killers', 'publicHD', 'mrs',
	 'net', 'com', 'patoghdl'
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
new_path = path.replace(str(path.split('/')[-1]),new_name)
os.rename(path, new_path)
print('The file has successfully been renamed to %s' % (new_name))
