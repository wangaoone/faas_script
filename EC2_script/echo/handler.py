import requests
from io import BytesIO
import time
import os
from threading import Thread
from time import sleep


def invoke(count):
    for j in range(count):
        start = time.time()
        fouput = os.popen(
            # 'curl -s http://ac7b9aeb5f98a11e8a65e0eb24347ff7-1866464858.us-east-1.elb.amazonaws.com:8080/function/echo -d "test"')
            'curl -s http://ad40972d1f9d811e8a65e0eb24347ff7-320729993.us-east-1.elb.amazonaws.com/scale')
            # 'curl -s http://ac7b9aeb5f98a11e8a65e0eb24347ff7-1866464858.us-east-1.elb.amazonaws.com:8080/function/echo')
        result = fouput.readline()
        print result
        if len(result) == 12:
        # if len(result) == 22:
            client_latency.append(time.time() - start)


class MyThread(Thread):
    """docstring for MyThread"""

    def __init__(self, count):
        super(MyThread, self).__init__()
        self.count = count

    def run(self):
        invoke(self.count)


def myThread(count):
    num = 25
    temp = count / num
    ths = []
    for thread in range(0, num):
        th = MyThread(temp)
        th.start()
        ths.append(th)
    for th in ths:
        th.join()
    client_latency.append("==============")


def main():
    # size = [100,200,300,400,500,600,700,800,900,1000]
    size = [5000]
    for j in size:
        # burst time
        start = time.time()
        # put burst workload to the thread to invoke
        myThread(j)
        perburst_time.append(time.time() - start)
        # inter-arrival
        # sleep(10)


if __name__ == "__main__":

    client_latency = []
    perburst_time = []
    base = os.path.dirname(__file__)

    start = time.time()
    main()
    total = time.time() - start

    fileObject = open(base + '/Total_time.txt', 'w')
    fileObject.write(str(total))
    fileObject.write('\n')
    fileObject.close()

    fileObject = open(base + '/response.txt', 'w')
    for i in client_latency:
        fileObject.write(str(i))
        fileObject.write('\n')
    fileObject.close()

    fileObject = open(base + '/burst.txt', 'w')
    for i in perburst_time:
        fileObject.write(str(i))
        fileObject.write('\n')
    fileObject.close()
