from mpi4py import MPI
import main_proc
import calc_proc

def main():
    comm = MPI.COMM_WORLD
    my_rank = comm.Get_rank()
    if(my_rank == 0):
        main_proc.start(comm)
    else:
        calc_proc.start(comm)
    

main()