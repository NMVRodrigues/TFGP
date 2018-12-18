import time
import threading


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

def add2(s):
	for i in range(0,10):
		s.append(2)
	

def add1(s):
    for i in range(0,10):
        s.append(1)
    

def main():
	#balance = threading.Value('i', 200)
    #lock = threading.Lock()
	temp = []
	d = threading.Thread(target=add1, args=(temp,))
	w = threading.Thread(target=add2, args=(temp,))
	d.start()
	w.start()
	d.join()
	w.join()
	print(temp)
	print(len(temp))


if __name__ == '__main__':
	main()