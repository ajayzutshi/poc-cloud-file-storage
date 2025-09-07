
import boto3
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    source_bucket = 'your-s3-bucket-name'
    backup_bucket = 'your-s3-backup-bucket'
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    files = s3.list_objects_v2(Bucket=source_bucket).get('Contents', [])
    
    for file in files:
        key = file['Key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(CopySource=copy_source, Bucket=backup_bucket, Key=f"{timestamp}/{key}")
    
    return {'status': 'Backup completed'}
