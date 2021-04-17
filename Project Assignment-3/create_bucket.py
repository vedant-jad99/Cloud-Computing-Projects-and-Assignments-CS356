#Creating an s3 bucket in aws
import boto3 as boto

BUCKET = open("bucket-name.txt").read().strip().lower()
s3 = boto.resource('s3')
s3.create_bucket(Bucket=BUCKET, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
