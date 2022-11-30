from mpi4py import MPI
from Point import *
import time

def measure_function_time(function):
    def inner(*agrs, **kwargs):
        start = time.time()
        result = function(*agrs, **kwargs)
        end = time.time()
        return result, {end - start}
    return inner

def get_amount_of_dots_in_circle(points):
    amount_of_points_inside_circle = 0
    for point in points:
        if (((1-2*point.x) ** 2 +(1-2*point.y) ** 2) <= 1):
            amount_of_points_inside_circle += 1
    return amount_of_points_inside_circle

@measure_function_time
def get_pi(points):
    return get_amount_of_dots_in_circle(points) / len(points) * 4

def start(comm):
    message = comm.recv(source = 0)
    pi, time = get_pi(message)
    comm.send(pi, dest = 0)
    comm.send(time, dest = 0)