#Creating an s3 bucket in aws
import boto3 as boto

s3 = boto.resource('s3')
s3.create_bucket(Bucket="ubunturekbucket1", CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})