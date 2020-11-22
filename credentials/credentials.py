import boto3
import pprint

# デフォルト
sts = boto3.client('sts')
pprint.pprint(sts.get_caller_identity())

# profile 使用
session = boto3.Session(profile_name='default')
sts = session.client('sts')
pprint.pprint(sts.get_caller_identity())
