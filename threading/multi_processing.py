## proceess that run in parallel
## CPU - BOUND tasks that are heavy on the CPU usage
## Parallel executinn of the multiple cores of the CPU

import multiprocessing
import time
def square_number():
    for i in range(5):
        time.sleep(1)   
        print(f"Squares :{i*i}")
def print_cubes():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cubes:{i*i*i}")
if __name__ =="__main__":
    ## create 2 processes
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=print_cubes)
    t = time.time()
    ## start the process
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    finishes_time = time.time() - t
    print(finishes_time)