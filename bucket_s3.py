import logging
import boto3
from botocore.exceptions import ClientError

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
    # s3 = boto3.client('s3')
    # s3.download_file('grupo2erikjuliana', OBJECT_NAME, 'FILE_NAME')
    arquivos = {'nome': []}
    conn = boto3.client('s3')  # again assumes boto.cfg setup, assume AWS S3
    for key in conn.list_objects(Bucket='grupo2erikjuliana')['Contents']:
        arquivos['nome'].append(key['Key'])
    return arquivos

def inserindo_bucket(my_array):
    client = boto3.client('s3')
    client.put_object(Body=my_array.file, Bucket='grupo2erikjuliana', Key=my_array.filename)