import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Top-Vacation-Spots') 
response =table.query(
    KeyConditionExpression=Key('Destination').eq('Bali')
    )

print(response)