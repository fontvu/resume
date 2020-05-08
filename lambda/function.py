import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('turingresume-counter')

response = table.get_item(
        Key={
            'year': ,
            'title': title
        }
)
