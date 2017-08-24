import shutil
import time
import sys
import os

class BackupMule(object):
	"""
	elements_to_save: 	number of elements that will be saved (progress bar)
	files_to_save: 		list of files, specified by the user, that need to be saved
	destination: 		list of destination(s) where you want your backups to be
	current_fold:		folder that is being backed up
	"""
	elements_to_save = 0
	saved_elements = 0
	files_to_save = []
	destinations = []
	current_fold = ""

	# initialize the Backup Mule
	def __init__(self, elements_to_save, files_to_save, destinations):
		self.elements_to_save = elements_to_save
		self.files_to_save = files_to_save
		self.destinations = destinations	
		print "[INFO] Beginning now..."
		print "[INF*] Skipping links!"
		print "[!DBG]", files_to_save
		print "[!DBG]", destinations

	
	# start backing up files and folders
	def start_backup(self):
		for addr in self.files_to_save:
			self.current_fold = ""
			self.save_it(addr)

	# save the file
	def save_it(self, src_addr):
		src_addr = src_addr.replace("\n", "") 		
		if os.path.isdir(src_addr):
			#print "[!DBG] IM IN", src_addr
			tmp_fold_addr = os.path.basename(src_addr)

			# get the correct location of sub-folders
			self.current_fold = str(self.current_fold) + '\\' +  tmp_fold_addr 
			#print "[!DBG] CURRENT", self.current_fold

			# create needed subfolders
			for dst_addr in self.destinations:
				#print "[!DBG] CREATED", dst_addr+self.current_fold
				folder_to_create = dst_addr + self.current_fold
				if not os.path.exists(folder_to_create):
					os.makedirs(folder_to_create)

			for file in os.listdir(src_addr):
				self.save_it(os.path.join(src_addr, file))
			self.current_fold = self.current_fold[:len(self.current_fold)-(len(tmp_fold_addr)+1)]	# remove the last folder from path as everything's saved
		elif os.path.islink(src_addr):
			pass
		else:
			for dst_addr in self.destinations:
				#sprint "[!DBG] SAVED FILE", src_addr, "to", dst_addr+self.current_fold
				shutil.copy2(src_addr, dst_addr+self.current_fold)
			self.saved_elements += 1
			#self.display_status()
	

	# display status on console
	def display_status(self):
		tmp = self.saved_elements
		sys.stdout.write('[')
		for i in range(self.elements_to_save):
			if tmp > 0:
				sys.stdout.write('#')
				tmp -= 1
			else:
				sys.stdout.write('-')
		sys.stdout.write(']')
		sys.stdout.write(str(self.saved_elements))
		sys.stdout.write(" out of ")
		sys.stdout.write(str(self.elements_to_save))		
		sys.stdout.flush()
		print ""
