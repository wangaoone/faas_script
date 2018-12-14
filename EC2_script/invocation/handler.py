import requests
from io import BytesIO
import time
import os
import sys
from threading import Thread
from time import sleep
import requests

# c4.8xlarge

def request(count):
    # URL = "http://a3f80df5eff2111e885690e4287844e2-1031646827.us-east-1.elb.amazonaws.com/hello-1"
    URL = "http://openfaas.k8s.tianium.com:8080/function/echo"
    for j in range(count):
        start = time.time()
        r = requests.get(URL)
        end = time.time()
        elapse = 0
        if r.headers.get('X-Duration-Seconds') != None :
            elapse = r.headers.get('X-Duration-Seconds')
        client_latency.append("{0},{1},{2},{3}".format(start, r.status_code, end - start, elapse))


class MyThread(Thread):
    """docstring for MyThread"""

    def __init__(self, count):
        super(MyThread, self).__init__()
        self.count = count

    def run(self):
        request(self.count)


def myThread(count):
    num = 1
    temp = count / num
    ths = []
    for thread in range(0, num):
        th = MyThread(temp)
        ths.append(th)
    for th in ths:
        th.start()
    for th in ths:
        th.join()


def main():
    # size = [100,200,300,400,500,600,700,800,900,1000]
    size = [2000]
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
