import boto3
# 1. Calls the resource() function in the boto3 module (which calls Session.resource('s3'))
# 2. Returns an S3.ServiceResource object in memory, and 's3' points to it
# 3. s3 is a vairable pointing to an object in memory that was created and returned when you call botos3.resource("s3")
s3 = boto3.resource("s3")
print(type(s3))
# <class 'boto3.resources.factory.s3.ServiceResource'>
print(s3)

method_list = dir(s3)
tools=[item for item in dir(s3) if not item.startswith("_")]
print(method_list)
print(tools)
