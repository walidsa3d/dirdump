import argparse
import os
import tablib
from fileinfo import fileinfo
import os
def listfiles(rootdir):
	f={}
	files=[]
	for dirName, subdirList, fileList in os.walk(rootdir):
	    for fname in fileList:
	    	f=os.path.abspath(os.path.join(dirName, fname))
	        files.append(fileinfo().basic(f))
	return files

def dump(file_list):
	data = tablib.Dataset(file_list)
	return data.json

print dump(listfiles('/home/walid/Desktop')) 


