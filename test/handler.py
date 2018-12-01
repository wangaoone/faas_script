import requests
from PIL import Image
from io import BytesIO
from memory_profiler import profile
import time
import os
from threading import Thread
from time import sleep


# @profile
def handle(req):
    response = requests.get(req)
    image = Image.open(BytesIO(response.content))

    print("If you get this shit, you finished")
    print(image.size)
    # opener = urllib.URLopener()
    # myurl = 'https://s3.amazonaws.com/demo.cs795.ao/test.jpg'
    # print opener.open(myurl)


def invoke(count):
    for j in range(count):
        start = time.time()
        fouput = os.popen(
            # 'curl -s http://a5f025492e1d411e8beb40e48a2251fe-1463939600.us-east-1.elb.amazonaws.com:8080/function/hellooo -d "https://s3.amazonaws.com/demo.cs795.ao/WechatIMG23.jpeg"')
            'curl -s http://a5f025492e1d411e8beb40e48a2251fe-250308801.us-east-1.elb.amazonaws.com:8080/function/echo -d "test"')
            # 'curl -s http://a5f025492e1d411e8beb40e48a2251fe-1463939600.us-east-1.elb.amazonaws.com:8080/function/echo -d "test"')
        result = fouput.readline()
        print result
        if len(result) == 22:
            client_latency.append(time.time() - start)


class MyThread(Thread):
    """docstring for MyThread"""

    def __init__(self, count):
        super(MyThread, self).__init__()
        self.count = count

    def run(self):
        invoke(self.count)


def myThread(count):
    num = 16
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
    # size = [128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]
    size = [1600]
    for j in size:
        # burst time
        start = time.time()
        # put burst workload to the thread to invoke
        myThread(j)
        perburst_time.append(time.time() - start)
        # inter-arrival
        sleep(10)


if __name__ == "__main__":
    # handle(
    #     "https://s3.amazonaws.com/demo.cs795.ao/WechatIMG23.jpeg")
    client_latency = []
    perburst_time = []

    start = time.time()
    main()
    total = time.time() - start

    fileObject = open('Total_time.txt', 'w')
    fileObject.write(str(total))
    fileObject.write('\n')
    fileObject.close()

    fileObject = open('response.txt', 'w')
    for i in client_latency:
        fileObject.write(str(i))
        fileObject.write('\n')
    fileObject.close()

    fileObject = open('burst.txt', 'w')
    for i in perburst_time:
        fileObject.write(str(i))
        fileObject.write('\n')
    fileObject.close()
