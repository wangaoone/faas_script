import requests
from PIL import Image
from io import BytesIO


def handle(req):
    response = requests.get(req)
    image = Image.open(BytesIO(response.content))
    print("size:", image.size)
