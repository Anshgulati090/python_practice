### Multithreading 
## I/O bound tasks, Concurent execution
import threading
import time
def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"the number is:{i}")
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"The letter are: {letter}")
#create 2 threads
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letters)
t = time.time()
#Start the thread
t1.start()
t2.start()
# Wait for the threads to complete

finished_time = time.time()-t
print(finished_time)
