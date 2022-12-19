import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Top-Vacation-Spots') 

response = table.scan()

print("The scan returned the following items:")
for item in response["Items"]:
    print(item)