# how to create or launch EC2 instance using boto3

import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-0b0dcb5097f052a63', 
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1)