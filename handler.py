import datetime
import json
import os
from io import BytesIO

import boto3
import PIL
from PIL import Image


def resized_image_url(resized_key, bucket, region):
    return "https://s3-{region}.amazonaws.com/{bucket}/{resized_key}".format(
        bucket=bucket, region=region, resized_key=resized_key
    )

def resize_image(bucket_name, key, size):
    size_split = size.split('x')
    s3 = boto3.resource('s3')
    obj = s3.Object(
        bucket_name=bucket_name,
        key=key,
    )
    obj_body = obj.get()['Body'].read()

    img = Image.open(BytesIO(obj_body))
    img = img.resize(
        (int(size_split[0]), int(size_split[1])), PIL.Image.ANTIALIAS
    )
    buffer = BytesIO()
    img.save(buffer, 'JPEG')
    buffer.seek(0)

    resized_key="{size}_{key}".format(size=size, key=key)
    obj = s3.Object(
        bucket_name=bucket_name,
        key=resized_key,
    )
    obj.put(Body=buffer, ContentType='image/jpeg')

    return resized_image_url(
        resized_key, bucket_name, os.environ["AWS_REGION"]
    )

def call(event, context):
    key = event["pathParameters"]["image"]
    size = event["pathParameters"]["size"]

    result_url = resize_image(os.environ["BUCKET"], key, size)

    response = {
        "statusCode": 301,
        "body": "",
        "headers": {
            "location": result_url
        }
    }

    return response
