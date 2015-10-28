import os

with open("c:/a.txt",'w') as f:
	for key in os.environ:
		
		#f.write('%s=%s\n'%(key,os.environ.get(key)))
		f.write('=','\n')