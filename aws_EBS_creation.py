# create AWS EBS volume from Snapshot using boto3 python

import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1c',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-036da9245a2ab2516',
    VolumeType='gp2')
