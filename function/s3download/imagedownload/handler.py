import boto3
import botocore
import requests


def handler(req):
    BUCKET_NAME = 'demo.cs795.ao'  # replace with your bucket name
    KEY = req  # replace with your object key

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
