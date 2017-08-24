"""
PY_BACKUP performs an incremental-backup of the specified files and folders.
Uses a log file to keep track of which and when folders have been saved.

$ python py_backup.py 

"""
import shutil
import time
import bum
import sys
import os

"""
ELEM_TO_SAVE:	count the files that are going to be saved
MAIN_SAVE:		contains the only the files specified by the user (inner files will be taken by the mule)
DESTINATION:	folders where files are going to be saved
"""
ELEM_TO_SAVE = 0
MAIN_SAVE = []
DESTINATION = []

def count_elements(url):
	global ELEM_TO_SAVE
	url = url.replace("\n", "")
	# print "URL is ", url, os.path.isdir(url)
	if os.path.isdir(url):
		for elem in os.listdir(url):
			count_elements(elem)
	else: 
		ELEM_TO_SAVE += 1

def main():
	# LOOK FOR THE LOG FILE
	try:
		ini_file = open("backup_y.ini", "r")
		print ""
		print "[INFO] INI File has been loaded"
	except IOError:
		print ""
		print "[WARN] No INI FILE: previous backups or specified folders and files have not been found"
		print "       File \"py_backup.log\" has been created; use it to specify what you want to save."
		print "       For example, an entry would be: /home/<username>/Documents"

		f = open("backup_y.ini", "w")
		f.write("[BACK UP]\n\n")
		f.write("[DESTINATION]\n")
		f.close()
		sys.exit()

	# COUNT THE NUMBER OF ELEMENTS TO BACKUP TO CREATE A PROGRESS BAR
	src_begins = 0
	dst_begins = 0
	for elem in ini_file:
		if elem == "[DESTINATION]\n":
			dst_begins = 1
			src_begins = 0
		elif elem == "[BACK UP]\n":
			src_begins = 1
			dst_begins = 0
		elif src_begins == 1 and dst_begins == 0:
			if not elem.isspace():
				count_elements(elem)
				MAIN_SAVE.append(elem.replace("\n", ""))
		elif src_begins == 0 and dst_begins == 1:
			if not elem.isspace():
				DESTINATION.append(elem.replace("\n", ""))
		else:
			pass

	print "[INFO] There are", ELEM_TO_SAVE, "Elements to Save"
	bck_mule = bum.BackupMule(ELEM_TO_SAVE, MAIN_SAVE, DESTINATION)
	bck_mule.start_backup()
	print "[INFO] DONE!"

if __name__ == '__main__':
	main()