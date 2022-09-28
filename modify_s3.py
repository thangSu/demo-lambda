import json
import boto3

dynamodb=boto3.resource('dynamodb')

def lambda_handler(event, context):
    primary_key={"studentcode": event["studentcode"]}
    table = dynamodb.Table("students")
    res = table.update_item(
        Key=primary_key,
        UpdateExpression="SET studentname= :studentname, schoolname= :schoolname",
        ExpressionAttributeValues={
            ":studentname": event["studentname"],
            ":schoolname" : event["schoolname"]
        })
    res1 = table.get_item(Key = primary_key)
    return {
        'full respone': res,
        'check_result': res1['Item']
    }
