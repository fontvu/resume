import boto3
import json

def handler(event, context):
    '''When this function is invoked - retrive visitor count, add one, store in database, return to client '''
    dynamodb = boto3.client('dynamodb')
    
    #Get Visits
    response = dynamodb.get_item(TableName='turingresumecounter', Key={'Site':{'N': '0'}})
    
    visits = int(response["Item"]["Visits"]["N"]) + 1

    visits = ['baar','baz']

    visits.l

    #Store Visits
    dynamodb.put_item(TableName='turingresumecounter', Item={'Site':{'N': '0'},'Visits':{'N': str(visits)}})
    
    return visits

