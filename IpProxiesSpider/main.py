import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)

def foo(tid):
    with sema:
        print('{0} acquire sema'.format(tid))
        wt = random() * 2
        time.sleep(wt)
    print('{} release sema'.format(tid))

def main():
    threads = []

    for i in range(5):
        t = Thread(target=foo, args=(i, ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()