import argparse
import os
import tablib
from fileinfo import fileinfo
import os

class dumpdir:

	def listfiles(self,rootdir):
		f={}
		files=[]
		for dirName, subdirList, fileList in os.walk(rootdir):
		    for fname in fileList:
		    	f=os.path.abspath(os.path.join(dirName, fname))
		        files.append(fileinfo().basic(f))
		return files

	def dump(self,file_list, forma):
		data = tablib.Dataset(file_list)
		if forma=="json":
			return data.json
		if forma=="csv":
			return data.csv
		if forma=="excel":
			return data.xlsx
		if forma=="xml":
			return ""
		if forma=="yaml":
			return data.yaml

	def write_To_File(self,filepath, data):
		with open(filepath,'w') as f:
			f.write(data)
	def main(self):
		parser = argparse.ArgumentParser(usage="-h for full usage")
		parser.add_argument('srcdir', help='source directory')
		parser.add_argument('destfile', help='destination file')
		parser.add_argument('-f', dest="exporttype", help='export format',required=True)
		args = parser.parse_args()
		files=self.listfiles(args.srcdir)
		dump=self.dump(files,args.exporttype)
		self.write_To_File(args.destfile,dump)
if __name__ == '__main__':
	dumpdir().main()

