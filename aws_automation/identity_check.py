import boto3

sts = boto3.client("sts")
identity = sts.get_caller_identity()
print(f"Userid: {identity['UserId']}")
print(f"Account: {identity['Account']}")
print(f"Arn: {identity['Arn']}")

