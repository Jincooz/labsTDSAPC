from threading import Thread
from time import sleep

def wait(amount_of_seconds, number_of_thread):
   print(f"{number_of_thread} start")
   sleep(amount_of_seconds)
   print(f"{number_of_thread} stop")

def main():
    threads = list()

    threads.append(Thread(target=wait,args=(1, 1)))
    threads.append(Thread(target=wait,args=(2, 2)))
    threads.append(Thread(target=wait,args=(4, 3)))
    threads.append(Thread(target=wait,args=(0.5, 4)))
    threads.append(Thread(target=wait,args=(0.01, 5)))
    threads.append(Thread(target=wait,args=(1.01, 6)))

    for thread in threads:
        thread.start()
    # треба дочекатися в головному потоці, щоб усі інші виконалися
    # так ми проходимо через усі потоки і чекаємо кінця їх виконання, якщо поток вже виконався затримки не буде
    # тобто альтернатино можна було не проходити через усі потоки а дочекатися тільки найдовшого з них 
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()