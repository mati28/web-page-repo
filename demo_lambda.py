import json

def lambda_handler(event,context):

    print("This is from lambda")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


#Bucket name must be unique accross all regions
# They must not contain uppercase character, underscore

User-based policy

IAM where w


What can you do?
IAM policies define what actions are allowed / denied on resources, and under what conditions.

Resources are the entities you create in AWS. i.e bucket

Policies get attached to Users, Roles or Groups

Who are you (temporarily)
A role is an IAM identity you can assume. It has permissions (via policies) and is intended to be used temporarily by users, services, or applications.
