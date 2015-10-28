from multiprocessing  import Process
import os 
def run(name):
	print("Run %s (%s) %s" % (name,os.getpid(),__name__))

if __name__ == '__main__':
	p = Process(target=run,args=("test",))
	p.start()
	#p.join()

print(__name__ )