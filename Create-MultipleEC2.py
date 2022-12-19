# create multiple EC2 instances boto3

import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-0bfdcb5067f052a63',
        InstanceType='t2.micro',
        MaxCount=3,
        MinCount=3)