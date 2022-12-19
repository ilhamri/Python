import boto3

client = boto3.client('dynamodb')

try:
    resp = client.delete_table(
        TableName="Top-Vacation-Spots"
    )
    print("Your table has been deleted")
except Exception as e:
    print("Error")
    print(e)