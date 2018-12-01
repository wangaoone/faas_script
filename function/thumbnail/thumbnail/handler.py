import requests
from PIL import Image
from io import BytesIO


def handle(req):
    response = requests.get(req)
    image = Image.open(BytesIO(response.content))
    temp = image.size
    size = (200, 300)
    image.thumbnail(size)
    print("size:", temp, image.size)
