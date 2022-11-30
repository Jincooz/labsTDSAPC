from mpi4py import MPI
import random
from Point import *
import time

def get_amount_of_dots():
    while True:
        try:
            amount_of_dots = int(input("Input amount of dots : "))
            break
        except:
            print("Error try again")
    return amount_of_dots

def start(comm):
    amount_of_dots = get_amount_of_dots()
    comm_size = comm.Get_size()
    dots = list()
    for _ in range(amount_of_dots):
        dots.append(Point(random.random(), random.random()))
    for procid in range(1, comm_size):
        send_amount_of_dots = int(amount_of_dots/(comm_size - 1) * procid)
        message = dots[0:send_amount_of_dots]
        comm.send(message, dest = procid)
    start = time.time()
    for procid in range(1, comm_size):
        f1  = time.time()
        pi = comm.recv(source = procid)
        f2 = time.time()
        ctime = comm.recv(source = procid)
        f3 = time.time()
        print(str(procid) + " programm end his work. His pi = " + str(pi) + ". Time = " + str(ctime) + ".")
        print(f"{f3-f2}s {f2-f1}s {f3-f1}s")
    end = time.time()
    print(f"I wait {end - start}s")