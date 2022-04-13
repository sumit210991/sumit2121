import boto3
import sys
import json
import logging
from botocore.exceptions import ClientError
import os

class SQSHelper(object):
    def __init__(self):
        self.client= boto3.client('sqs',region_name='us-east-1', aws_access_key_id='AKIAZBFXZ5ZYPL4YQS4X',
                               aws_secret_access_key='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')
        self.queue = self.client.create_queue(QueueName='assignmentqueue')
        url=self.client.get_queue_url(QueueName='assignmentqueue')
        self.queue_url=url['QueueUrl']
        

    def send_message(self, Message={}):
        try:
            data=json.dumps(Message)
            response = self.client.send_message(QueueUrl=self.queue_url, MessageBody=json.dumps(Message) 
            #,MessageAttributes={'message_type':{
            #'DataType': 'String',
            #'StringValue': message_type}}
            )
        except ClientError as ex:
             logging.error(ex)
             return False
        return True