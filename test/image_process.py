import requests
from PIL import Image
from io import BytesIO
from memory_profiler import profile
import time


def handle(req):
    response = requests.get(req)
    image = Image.open(BytesIO(response.content))
    temp = image.size
    size = (200, 300)
    image.thumbnail(size)
    print("size:", temp, image.size)


if __name__ == '__main__':
    print("load the image..")
    req = 'https://s3.amazonaws.com/demo.cs795.ao/WechatIMG23.jpeg'
    start = time.time()
    handle(req)
    print(time.time() - start)
