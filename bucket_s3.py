import logging
import boto3
from botocore.exceptions import ClientError
import io
import pickle

def criando_bucket():

    bucket_name = 'grupo2erikjuliana'
    region = None
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def lendo_bucket():
    pass

import gzip, io

def gzip_greet_file(fileobj):
    """write gzipped hello message to a file"""
    with gzip.open(filename=fileobj, mode='wb') as fp:
        fp.write(b'hello!')

def inserindo_bucket(my_array):
    client = boto3.client('s3')
    client.put_object(Body=my_array.file, Bucket='grupo2erikjuliana', Key=my_array.filename)