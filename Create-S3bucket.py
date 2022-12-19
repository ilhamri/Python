#!/usr/bin/env python3
import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("faali")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
   
)
print(response) 