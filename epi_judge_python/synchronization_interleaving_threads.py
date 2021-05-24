import threading

oddCheck =  threading.Condition()
evenCheck = threading.Condition()

def even_thread(x):
	
	for i in range(x):
		
		if i % 2 == 0:
			evenCheck.acquire()
			evenCheck.wait()
			evenCheck.release()
			print(i)
			oddCheck.acquire()
			oddCheck.notify()
			oddCheck.release()

def odd_thread(x):
	for i in range(x):
		if i % 2 == 1:
			oddCheck.acquire()
			oddCheck.wait()
			oddCheck.release()
			print(i)
			evenCheck.acquire()
			evenCheck.notify()
			evenCheck.release()

def main():
	odd = threading.Thread(target=odd_thread, args=(100,))
	even = threading.Thread(target=even_thread, args=(100,))


	odd.start()
	even.start()

	evenCheck.acquire()
	evenCheck.notify()
	evenCheck.release()

main()