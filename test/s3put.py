import boto3
import botocore
from PIL import Image
from StringIO import StringIO
import requests


def upload():
    s3 = boto3.resource("s3")
    bucket = 'demo.cs795.ao'
    data = open('test.jpg', 'rb')
    s3.Bucket(bucket).put_object(Key='test.jpg', Body=data)


def download():
    BUCKET_NAME = 'demo.cs795.ao'  # replace with your bucket name
    KEY = 'test.jpg'  # replace with your object key

    s3 = boto3.resource('s3')
    client = boto3.client('s3')

    try:

        # s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')

        print client.get_object(Bucket=BUCKET_NAME, Key=KEY)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


def urlDownload():
    url = 'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=af9770bd5b66d0167e19992eaf10b33a/5243fbf2b211931326320cc06c380cd791238d49.jpg'
    image = Image.open(StringIO(requests.get(url, stream=True).raw.read()))
    image.show()


if __name__ == "__main__":
    # urlDownload()
    urlDownload()
