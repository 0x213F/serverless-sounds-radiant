import boto3
import os


def _setup_boto3_client(session):
    try:
        region_name = os.environ['BOTO3_REGION_NAME']
        endpoint_url = os.environ['BOTO3_ENDPOINT_URL']
        aws_access_key_id = os.environ['BOTO3_ACCESS_KEY']
        aws_secret_access_key = os.environ['BOTO3_SECRET_KEY']
    except KeyError:
        return {
            "success": False,
            "message": "Misconfigued environment variables"
        }
    return session.client(
        "s3",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def _get_email_subcribers_using_boto3(session, client):
    '''
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2
    '''
    bucket = "sounds-radiant"
    prefix = "private/email-subscribers/"
    obj = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    # Get all "local filenames"
    return [c['Key'][len(prefix):] for c in obj['Contents']]


def main(args):
    boto3_session = boto3.session.Session()
    boto3_client = _setup_boto3_client(boto3_session)

    email_subscribers = _get_email_subcribers_using_boto3(boto3_session, boto3_client)
    name = args.get("name", "Sounds Radiant")
    greeting = "Hello " + name + "!"
    print(greeting)
    return {"body": greeting}
