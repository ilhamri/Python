import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Top-Vacation-Spots')
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'Destination': 'Mecca',
            'Ranking': 1,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Medina',
            'Ranking': 2,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Maldives',
            'Ranking': 3,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Malaysia',
            'Ranking': 4,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Tanzania',
            'Ranking': 5,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Ogadenia',
            'Ranking': 6,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Al Aqsa',
            'Ranking': 7,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'LA',
            'Ranking': 8,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Bali',
            'Ranking': 9,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Baniff',
            'Ranking': 10,
        }
    )
print("Items Successfully Added")
