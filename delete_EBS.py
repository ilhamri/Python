# how to delete EBS volume Snapshot using boto3 python

import boto3
ec2_client=boto3.client("ec2")
ec2_client.delete_snapshot(SnapshotId='snap-026da9505a2ab2516')
