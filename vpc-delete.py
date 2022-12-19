# how to delete VPC with Python
import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId='string' #enter VPC ID here
)