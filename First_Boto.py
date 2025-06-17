import boto3

# Create EC2 client 
ec2_client = boto3.client('ec2', region_name='us-east-1')  

# Launch instance
response = ec2_client.run_instances(
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

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']
print("Instance ID:", instance_id)

# Wait until it's running
ec2_resource = boto3.resource('ec2', region_name='us-east-1')
instance = ec2_resource.Instance(instance_id)
instance.wait_until_running()

# Reload instance data to get public IP
instance.load()
print("Public IPv4:", instance.public_ip_address)
