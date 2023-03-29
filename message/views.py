from django.http import HttpResponse
import boto3
import json
def home(request):
   


# Create an SNS client
    sns = boto3.client('sns', 
                   aws_access_key_id='API KEY',
                   aws_secret_access_key='SECRET ACCESS KEY',
                   region_name='REGION')

# Publish an SMS message to the SNS topic
    response = sns.publish(
   
    Message='Hello from AWS SNS!',
    MessageAttributes={
        'AWS.SNS.SMS.SMSType': {
            'DataType': 'String',
            'StringValue': 'Transactional'
        },
        'AWS.SNS.SMS.SenderID': {
            'DataType': 'String',
            'StringValue': 'MySenderID'
        }
    },
    PhoneNumber='NUMBER'# The number to wwhich you want to send sms
    )
    res=json.dumps(response)
    print(response)
    return HttpResponse(res)

