import boto3
session = Ses
ec2_console = boto3.client('ec2')

response = ec2_console.run_instances(
    ImageId='ami-09e6f87a47903347c',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'Ec2_Boto3'}
            ]
        }
    ]
)

