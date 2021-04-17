#!/usr/bin/env python3
#Testing basic label detection using aws rekognition

import boto3 as boto
import logging

#Setting basic logger config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(threadName)s', filename="test.log", filemode="a")

#Detecting labels from images
def detect_labels(bucket, key, max_labels=20, min_confidence=90, region="us-east-2"):
    logging.info("Starting rekognition service")
    rekognition = boto.client("rekognition", region)
    try:
        response = rekognition.detect_labels(
        Image={
            "S3Object": {
    	    "Bucket": bucket,
    	    "Name": key,
            }
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence)
        logging.info("Response received")
        return response['Labels']
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    labels = detect_labels("ubunturekbucket1", "test.jpg")
    print(labels)
    for label in labels:
        logging.warning("Output: {Name} - {Confidence}".format(**label))
