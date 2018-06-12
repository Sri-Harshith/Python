import threading
import os
def squ(a):
	print('the name is {}'.format(threading.current_thread().name))
	print('the process id for {}'.format(threading.current_thread().name,os.getpid()))
	print('the square of the number is {}'.format(a*a))
def cube(a):
	print('the name is {}'.format(threading.current_thread().name))
	print('the process id for {}'.format(threading.current_thread().name,os.getpid()))
	print('the square of the number is {}'.format(a*a*a))

if __name__ == '__main__' :
	# squ(2)
	# cube(2)
	print('the thread name is {}'.format(threading.current_thread().name))
	print('the process id for {} is {}'.format(threading.current_thread().name,os.getpid()))

	thread1 = threading.Thread(target = squ,args= (2,))
	thread2 = threading.Thread(target = cube,args= (2,))

	thread1.start()
	thread2.start()