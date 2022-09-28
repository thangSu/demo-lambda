import json
import boto3
def lambda_handler(event, context):
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('students')
    res= table.put_item(
        Item={
            'studentcode': event["params"]["querystring"]["studentcode"],
            'studentname': event["params"]["querystring"]["studentname"]
        }
        )
        
    return {
        'statusCode': res,
    }
