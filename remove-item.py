import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Top-Vacation-Spots') 
response = table.delete_item(
        Key={
            'Destination': 'Mecca', 'Ranking': 1
        }
    )
print(response)