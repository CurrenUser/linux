import os, time

pid = os.fork()
if pid:
    while(True):
        print(f'i am the parent, child is pis:{pid}')
        time.sleep(120)
else:
    print(f'i am the child')
    time.sleep(1000)