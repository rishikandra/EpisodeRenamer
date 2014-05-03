<h1>Episode Renamer</h1>
<p>Most of us download TV shows from the internet. These are very poorly named with generally no mention of the title given to the episode by its creators.

This script aims at renaming the episodes to a proper format. It does so by extractin the show name, season and episode number from the current file name and then connecting to a web api where it searches for the title of the corresponding episode.
</p>
The script renames the file to the following format:</br>
	Show_name - SxxExx - Episode_title

Requirements:</br>
	1. Python 3.x
	2. pytvdbapi

To install pytvdbapi, use "pip install pytvdbapi" (might need administrator privileges)

Instructions:</br>
	For Linux/Unix users:</br>
		1. Open terminal and change directory to where the episode is located.
		2. Assuming your EpisodeRenamer.py file is in the home directory, Run: python ~/EpisodeRenamer.py File_name (make sure you get the file name and extension right).
		3. Et viola.

	For Windows users:</br>
		1. Start menu -> run -> cmd
		2. Navigate to the folder where the episode is located.
		3. Assuming your EpisodeRenamer-win.py is in "C:\Python34", Run: python "C:\Python34\EpisodeRenamer-win.py" File_name (make sure you get the file name and extension right).
		4. Et viola.

Please contact me at rishikandra11@gmail.com if you have any queries or suggestions.