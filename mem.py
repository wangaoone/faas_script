import os
import sys
from time import sleep
import time
from threading import Thread
import numpy as np


def normal_dis(mu, sigma, population):
    np.random.seed(0)
    s = np.random.normal(mu, sigma, population)
    return s


def invoke(count):
    # Generate burst size and number of function call per burst [100,200,300,400...,900,1000] size 10
    # argv[1] = count control the amount of element in the array.
    for j in range(count):
        start = time.time()
        fouput = os.popen(
            'curl -s http://a5f025492e1d411e8beb40e48a2251fe-1463939600.us-east-1.elb.amazonaws.com:8080/function/hellooo -d "https://s3.amazonaws.com/demo.cs795.ao/WechatIMG23.jpeg"')
        result = fouput.readlines()

        if result == ['If you get this shit, you finished\n', '(3000, 2000)\n']:
            print("true");
        else:
            print("false")

        end = time.time()
        client_latency.append(end - start)


class MyThread(Thread):
    """docstring for MyThread"""

    def __init__(self, count):
        super(MyThread, self).__init__()
        self.count = count

    def run(self):
        invoke(self.count)


def myThread(count):
    # Four threads
    # temp = count / 4
    thread_1 = MyThread(count)
    thread_2 = MyThread(count)
    # thread_3 = MyThread(temp)
    # thread_4 = MyThread(temp)
    thread_1.start()
    thread_2.start()
    # thread_3.start()
    # thread_4.start()


# @profile
def main(argv):
    # # Generate normal distributed
    # normal = normal_dis(float(argv[2]), float(argv[3]), int(argv[4]))  # normal_dis(128, 0.9, 100)
    # print normal

    # # Generate Memory
    # mem = [1] * ((1024 * 1024) * int(argv[1]))  # 8 * argv mb

    count = int(argv[1])
    intertime = int(argv[2])

    # Control the number of burst. Burst size = 100,200,300,400,500
    burst = [0 for i in range(count)]
    for i in range(count):
        burst[i] = 100 * (i + 1)  # Generate [1,2...]* 100 or ___
        print "The burst size is %d" % burst[i]

    # for i in range(times):
    for j in range(3):
        myThread(j)
        # if j != burst[-1]:
        sleep(intertime)


if __name__ == "__main__":
    client_latency = []
    # start = time.time()
    main(sys.argv)
    # end = time.time()
    # print "The total time is %s" % str(end - start)
    # print "The start time is %s" % str(end - start)
    # print "The end time is %s" % str(end)
    sleep(15)
    print client_latency
    print len(client_latency)
