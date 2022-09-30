import json
import boto3
dynamodb = boto3.resource("dynamodb")
def lambda_handler(event, context):
    table = dynamodb.Table("students")
    primary_key = {"studentcode": event["studentcode"]}
    
    res = table.delete_item(Key= primary_key);
    return {
        'statusCode': res
    }
