Hw27.10
# How to start on Linux
You need instaled python3, pip3 and some MPI implementaition</br>
Download this repository to your machine</br>
```
git clone https://github.com/Jincooz/labsTDSAPC.git
```
Checkout to branch 4-th_homework(27.10)</br>
```
git checkout 'origin/4-th_homework(27.10)'
```
You need instaled python3 and pip3</br>
After this open in console folder hw27.10</br>
Run this comand to install needed external modules
```
pip3 install -r requirements.txt 
```
Wait till them download</br>
As MPI implementation i use MPICH</br>
So now you can start this program using this comand</br>
```
mpirun -np 2 python3 main.py
```