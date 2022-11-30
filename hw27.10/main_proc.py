from mpi4py import MPI
import random
from Point import *

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
    for procid in range(1, comm_size):
        pi = comm.recv(source = procid)
        ctime = comm.recv(source = procid)
        print(str(procid) + " programm end his work. His pi = " + str(pi) + ". Time = " + str(ctime) + ".")