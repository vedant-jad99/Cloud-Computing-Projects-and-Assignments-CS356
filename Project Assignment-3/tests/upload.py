#!/usr/bin/env python3
#Testing basic upload to s3 bucket

import boto3 as boto
import logging

#Setting basic logger config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(threadName)s', filename="test.log", filemode="a")

#Opening and checking image
def open_img(filename):
    data = open(filename, 'rb')
    logging.info('data '+ str(data))
    return data

#Opening and uploading to s3 bucket
def upload_to_s3(filename):
    s3 = boto.resource('s3')
    try:
        data = open_img(filename)
        s3.Bucket('ubunturekbucket1').put_object(Key="test.jpg", Body=data)
        logging.info("Upload successful!")
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    upload_to_s3("test.jpg")
