# This is a sample Python script.
import logging
import os
import yaml
from botocore.exceptions import ClientError
from colorama import Fore
from aws.envsetup.config import client, resource

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


# ------------------------------------------------------------------------------------------------------------


def createSecurityGroup():
    vpc = resource("ec2").create_vpc(CidrBlock='10.0.0.0/24')

    responesVPC = "{}".format(vpc.id)

    secure = client("ec2").create_security_group(DryRun=False,
                                                 GroupName='testGroup',
                                                 Description="Test 22 ssh",
                                                 VpcId=responesVPC)

    print(secure['GroupId'])


def describeSecurityGroups():
    request = client("ec2").describe_security_groups()

    print(request)


def vpcCreation(cdir="10.0.0.0/24"):
    vpc = client("ec2").create_vpc(CidrBlock=cdir)
    return vpc


def checkImages():
    print("Getting Information .....")

    instances_image = resource().connect().describe_images()

    for int in instances_image['Images']:
        print("\n" + yaml.dump(int['ImageId']))


def create_VPCID():
    vpc = client("ec2").create_vpc('10.0.0.0/24')

    print(vpc.id)


def create_VPCID3():
    vpc = resource("ec2").create_vpc(CidrBlock='10.0.0.0/24')

    return print("{}".format(vpc.id))


def delete_VPCID3():
    vpc = client("ec2").describe_vpcs()

    for i in vpc['Vpcs']:
        print(yaml.dump(i))

    # list_vpcs = []

    user_input = input("\nEnter VpcId to be deleted: ")

    if user_input:

        vpc_delete = client("ec2").delete_vpc(VpcId=user_input)

    else:
        print("Wrong information ")
    return True


def createInstance(

        keyname="drum11132",
        groupname="john_security1234",
        cidr="10.0.0.0/24"
):
    # Set up our logger
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger()

    # KeyFiles
    keyDir = "/tmp/"
    keyFileFormat = ".pem"
    keyFile = keyDir + keyname + keyFileFormat

    try:

        request = client("ec2").describe_security_groups(GroupNames=[groupname])

    except ClientError as e:

        if e.response['Error']['Code'] == "InvalidGroup.NotFound":
            print("[+] Dry Run successful .... ")

        elif e.response['Error']['Code'] == "InvalidGroup.NotFound":
            print("[+] Creating security group for %s" % groupname)
            get_vpc = client("ec2").create_vpc(cidrBlock="10.0.0.0/24")
            securityGroupCreation = client("ec2").create_security_groups(DryRun=True, GroupNames=groupname,
                                                                         Description='Test server security group',
                                                                         VpcId=get_vpc.id)

            response = client("ec2").authorize_egress(
                DryRun=False,
                SourceSecurityGroupName=groupname,
                SourceSecurityGroupOwnerId=securityGroupCreation['GroupId'],
                IpProtocol='tcp',
                FromPort=22,
                ToPort=22,
                CidrIp=cidr
            )

    # Set up connection

    try:

        keysCreation = client("ec2").create_key_pair(KeyName=keyname)
        print("\n[+] Creating KeyPair for %s" % keyname)
        private_key = keysCreation['KeyMaterial']
        # Props to learnaws.org
        with os.fdopen(os.open(keyFile, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as e:
            e.write(private_key)


    except ClientError as e:

        if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
            logger.warning(' Duplicate Key Error (InvalidKeyPair)...')
        else:
            raise e

    server = client("ec2").run_instances(
        DryRun=False,
        ImageId=ImageIdUbuntu[0],
        MinCount=1,
        MaxCount=1,
        KeyName=keyname,

        UserData='/home/xza1/PycharmProjects/LeftSide/aws/ec2/GeneralStartupScript.sh',
        InstanceType='t2.medium',

        Placement={
            'AvailabilityZone': 'us-west-2b',
            'Tenancy': 'default'
        },

        BlockDeviceMappings=[
            {
                'VirtualName': 'string',
                'DeviceName': '/dev/sdh',
                'Ebs': {
                    'VolumeSize': 50,
                    'DeleteOnTermination': True,
                    'VolumeType': 'standard',
                    'Encrypted': False
                },

            },
        ],

        Monitoring={
            'Enabled': False,
        })

    for instance in server['ec2']:
        print(yaml.dump(instance))
        instanceId = instance['InstanceId']

        tag = client("ec2").create_tags(
            DryRun=False,
            Resources=[
                instanceId],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': keyname
                },
            ]
        )


def keys102(groupname="testGroup1"):
    get_vpc = resource("ec2").create_vpc(CidrBlock='10.0.0.0/24')

    request = client("ec2").create_security_group(DryRun=False, GroupName=groupname,
                                                  Description='Test server security group', VpcId=get_vpc.id)
    print(request)


def createKeyPairs(keyname):
    keyDir = "/tmp/"
    keyFileFormat = ".pem"
    keyFile = keyDir + keyname + keyFileFormat
    getKeys()

    try:

        keysCreation = client("ec2").create_key_pair(KeyName=keyname)
        print("\n[+] Creating KeyPair for %s" % keyname)
        private_key = keysCreation['KeyMaterial']
        # Props to learnaws.org
        with os.fdopen(os.open(keyFile, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as e:
            e.write(private_key)


    except ClientError as e:

        if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
            logger.warning(' Duplicate Key Error (InvalidKeyPair)...')

        else:
            raise e


def startInstance():
    getList_instances = client("ec2").describe_instances()

    getinstanceId = input("Enter InstanceId to start: ")

    start = client("ec2").start_instances(InstanceIds=[getinstanceId], DryRun=False)
    print(getList_instances)


# noinspection DuplicatedCode
def getInstances():
    request = client("ec2").describe_instances()
    # print(yaml.dump(request))
    # print(request)
    for i in request['Reservations']:
        for k in i['Instances']:
            print("\nKeyName: {}".format(k['KeyName']),
                  "\nInstanceId: {}".format(k['InstanceId']),
                  "\ninstanceType: {} ".format(k['InstanceType']),
                  "\nImageId: {}".format(k['ImageId']),
                  "\nMonitoring: {}".format(k['Monitoring']),
                  "\nPrivateIpAddress: {}".format(k['PrivateIpAddress']),
                  "\nPrivateDnsName: {}".format(k['PrivateDnsName']),
                  "\nPublicDnsName: {}".format(k['PublicDnsName']),
                  "\nState: {}".format(k['State']),
                  "\nVpcId: {}".format(k['VpcId']),
                  "\nLaunchTime: {}".format(k['LaunchTime'])
                  )


def stop_Instances(instance):
    getInstances()
    # instance = input("\nEnter the id of instance to be stopped: ")

    request = client("e2").describe_instances()

    for i in request['Reservations']:
        for k in i['ec2']:
            if k['InstanceId'] == instance:
                stopInst = resource("ec2").instances.filter(InstanceIds=[instance]).stop()
                print("Instance stopping : %s " % instance)
            else:
                for status in resource("ec2").meta.client.describe_instance_status(InstanceId=[instance])[
                    'InstanceStatuses']:
                    print(status['state-name-status'])


def start_Instances(instance):
    getInstances()
    # instance = input("\nEnter the id of instance to be stopped: ")

    request = client("ec2").describe_instances()

    for i in request['Reservations']:
        for k in i['Instances']:
            if k['InstanceId'] == instance:
                stopInst = resource("ec2").instances.filter(InstanceIds=[instance]).start()
                print("Instance starting : %s " % instance)
            else:
                for status in resource("ec2").meta.client.describe_instance_status(InstanceIds=[instance])[
                    'InstanceStatuses']:
                    print(status['state-name-status'])


def delete_Instances():
    getInstances()
    instance = input("\nEnter the id of instance to be stopped: ")

    request = client("ec2").describe_instances()

    for i in request['Reservations']:
        for k in i['ec2']:
            if k['InstanceId'] == instance:
                stopInst = resource("ec2").instances.filter(InstanceIds=[instance]).terminate()
                print("Instance stopping : %s " % instance)
            else:
                for status in resource("ec2").meta.client.describe_instance_status(InstanceId=[instance])[
                    'InstanceStatuses']:
                    print(status['state-name-status'])


def getKeys():
    getKeyInfos = client("ec2").describe_key_pairs()

    for key in getKeyInfos['KeyPairs']:
        # import yaml
        # print(yaml.dump(key))
        print("\nKeyName: {}".format(key['KeyName']),
              "\nKeyPairId: {}".format(key['KeyPairId']),
              "\nKeyFingerprint: {}".format(key['KeyFingerprint'])
              )


def deleteKeyPairs(keyname):
    getKeys()
    try:

        deleteKey = client("ec2").delete_key_pair(KeyName=keyname)

    except ClientError as e:
        if e.response['Error']['Code'] == "InvalidKeyPair.NotFound":
            logger.warning("NonExisting Keyname: %s" % keyname)

        else:
            raise e


def aws_list_buckets():
    listBuckets = client("s3").list_buckets()
    for bucket in listBuckets['Buckets']:
        print("\nBuckName: {}".format(bucket['Name']),
              "\nCreationDate: {}".format(bucket['CreationDate']))


def aws_create_bucket(bucketName, region='us-west-2'):
    location = {'LocationConstraint': region}

    try:
        if region is None:
            client("s3").create_bucket(Bucket=bucketName)
        else:
            # connect = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            client("s3").create_bucket(Bucket=bucketName,
                                       CreateBucketConfiguration=location)

    except ClientError as e:
        logger.error(e)
        return False
    return True


def aws_upload_bucket(fileName, bucketName, objectName=None):
    if objectName is None:
        objectName = fileName

        try:
            resource("s3").Bucket(bucketName).upload_file(fileName, objectName)
        except ClientError as e:
            logger.error(e)
            return False
        return True


def aws_download_bucket(bucketName, fileName, objectName=None):
    if objectName is None:
        objectName = fileName

        try:
            #            s3://bucketName/objectName  '/tmp/filename'
            #  Download s3://bucket/key to /tmp/myfile
            resource("s3").Bucket(bucketName, objectName).download_file(fileName)
        except ClientError as e:
            logger.error(e)
            return False
        return True


def aws_delete_bucket(bucketName):
    # list_buckets()
    try:
        bucket = resource("s3").Bucket(bucketName)

        for buc in bucket.objects.all():
            buc.delete()
        bucket.delete()

    except ClientError as e:
        logger.error("Check ... %s" % e)
        return False
    return True


def getAcl():
    bucket_acl = resource("s3").BucketAcl('kanada11')
    print(bucket_acl)


def upload_object(filename, bucketName, key):
    resource("s3").Object(bucketName, key).put(Body=open(filename, 'rb'))


def downloadAws(bucketName, objectName, filePath):
    # if filePath is None:
    #	filePath = "/tmp"

    try:
        #            s3://bucketName/objectName  '/tmp/filename'
        #  Download s3://bucket/key to /tmp/myfile
        resource().Bucket(bucketName).download_file(objectName, filePath)
    except ClientError as e:
        logger.error(e)
        return False
    return True


def testExists(bucketName):
    bucket = resource("s3").Bucket(bucketName)

    # exists = True

    try:
        bucket.meta.client.head_bucket(Bucket=bucketName)
    except ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            # exists = False
            logger.error("Does not exists")


class IAM_USER:

    def __init__(self):
        # self.username = input("Enter the username")
        # self.connect = AWSConnect.client("iam")
        pass

    def create_iam_user(self):

        user = client("iam").create_user(UserName=self)
        print(user)

    def getUsers(self=2):

        user = client("iam").list_users(MaxItems=self)

        import yaml
        print(yaml.dump(user))

    def update_iam_user(self, newUser):

        user = client("iam").update_user(UserName=self, NewUserName=newUser)
        print(user)

    def delete_iam_user(self):

        try:
            user = client("self").create_user(UserName=self)
            print(user)

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True

    def create_key(self):

        try:
            user = client("iam").create_access_key(UserName=self)
            for key in user:
                print(key['AccessKey'])

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True

    def delete_key(self, accessKeyId):

        try:

            user = client("iam").delete_access_key(UserName=self, AccessKeyId=accessKeyId)
            print(user)

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True

    def getKeys(self, maxItems=10):

        try:
            user = client("iam").list_access_keys(UserName=self, MaxItems=maxItems)
            for ids in user['AccessKeyMetadata']:
                print("\n {}".format(ids['UserName']),
                      "\n {}".format(ids['AccessKeyId']),
                      "\n {}".format(ids['Status'])
                      )

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True

    def createPolicy(self):

        pass

    def getPolicy(self):

        getPols = client("iam").list_policies(Scope=self, MaxItems=10)
        for pols in getPols['Policies']:
            print(yaml.dump(pols))


def create_loginProfile(self, password):
    Filename = "/tmp/" + self + "_loginProfileDoc.txt"
    try:
        user = resource("iam").create(self)
        login_profile = user.create_login_profile(Password=password, PasswordResetRequired=True)
        print(login_profile)

        with open(Filename, "w") as kg:
            print(login_profile, file=kg)

    except ClientError as e:
        if e.response['Error']['Code'] == "EntityAlreadyExists":
            logger.error("Entity Exists")
            return False
        return True


def checkLogs(self):
    user = resource("iam").groups.all()
    name = resource("iam").User(self)
    for g in user:
        print(g)
        group = name.add_group(GroupName='AdminLetfside')
        print(group)


def test_createInstance(

        keyname="TopRA",
        groupname="TopRA_security",
        cidr="10.0.0.0/24"
):
    from botocore import exceptions

    # KeyFiles
    keyDir = "/tmp/"
    keyFileFormat = ".pem"
    keyFile = keyDir + keyname + keyFileFormat

    try:

        request = client("ec2").describe_security_groups(GroupNames=[groupname])

    except exceptions.ClientError as e:

        if e.response['Error']['Code'] == "InvalidGroup.NotFound":
            print("[+] Dry Run successful .... ")

        elif e.response['Error']['Code'] == "InvalidGroup.NotFound":
            print("[+] Creating security group for %s" % groupname)
            get_vpc = client("ec2").create_vpc(cidrBlock="10.0.0.0/24")
            securityGroupCreation = client("ec2").create_security_groups(DryRun=True, GroupNames=groupname,
                                                                         Description='Test server security group',
                                                                         VpcId=get_vpc.id)

            response = client("ec2").authorize_egress(
                DryRun=False,
                SourceSecurityGroupName=groupname,
                SourceSecurityGroupOwnerId=securityGroupCreation['GroupId'],
                IpProtocol='tcp',
                FromPort=22,
                ToPort=22,
                CidrIp=cidr
            )

    try:

        keysCreation = client("ec2").create_key_pair(KeyName=keyname)
        print("\n[+] Creating KeyPair for %s" % keyname)
        private_key = keysCreation['KeyMaterial']
        # Props to learnaws.org
        with os.fdopen(os.open(keyFile, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as e:
            e.write(private_key)


    except exceptions.ClientError as e:

        if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
            logger.warning(' Duplicate Key Error (InvalidKeyPair)...')
        else:
            raise e

    server = client("ec2").run_instances(
        DryRun=False,
        ImageId=ImageIdUbuntu[0],
        MinCount=1,
        MaxCount=1,
        KeyName=keyname,

        UserData='/home/xza1/PycharmProjects/LeftSide/aws/Instances/GeneralStartupScript.sh',
        InstanceType='t2.medium',

        Placement={
            'AvailabilityZone': 'us-west-2b',
            'Tenancy': 'default'
        },

        BlockDeviceMappings=[
            {
                'VirtualName': 'string',
                'DeviceName': '/dev/sdh',
                'Ebs': {
                    'VolumeSize': 50,
                    'DeleteOnTermination': True,
                    'VolumeType': 'standard',
                    'Encrypted': False
                },

            },
        ],

        Monitoring={
            'Enabled': False,
        })

    for instance in server['Instances']:
        print(yaml.dump(instance))
        instanceId = instance['InstanceId']
        instanceIP = instance['PublicDnsName']

        tag = client("ec2").create_tags(
            DryRun=False,
            Resources=[
                instanceId],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': keyname
                },
            ]
        )

        import time
        import paramiko

        terminal = resource("ec2").Instance(instanceId)
        terminal.wait_until_running()
        time.sleep(3)

        paramikoKey = paramiko.RSAKey.from_private_key_file(keyFile)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_client.connect(hostname=instanceIP, username="ubuntu", pkey=paramikoKey)

        stdin, stdout, stderr = ssh_client.exec_command("sudo apt-get -y update")
        print(stdout.read())
        print(stderr.read())
        ssh_client.close()


def grabInstances():
    request = client("ec2").describe_instances()
    # print(yaml.dump(request))
    # print(request)
    for i in request['Reservations']:
        for k in i['Instances']:
            print("\nKeyName: {}".format(k['KeyName']),
                  "\nInstanceId: {}".format(k['InstanceId']),
                  "\ninstanceType: {} ".format(k['InstanceType']),
                  "\nImageId: {}".format(k['ImageId']),
                  "\nMonitoring: {}".format(k['Monitoring']),
                  # "\nPrivateIpAddress: {}".format(k['PrivateIpAddress']),
                  "\nPrivateDnsName: {}".format(k['PrivateDnsName']),
                  "\nPublicDnsName: {}".format(k['PublicDnsName']),
                  "\nState: {}".format(k['State']),
                  # "\nVpcId: {}".format(k['VpcId']),
                  "\nLaunchTime: {}".format(k['LaunchTime'])
                  )


def onInstance():
    grabInstances()
    # instance = input("\nEnter the id of instance to be stopped: ")

    request = client("ec2").describe_instances()

    for i in request['Reservations']:
        for k in i['Instances']:
            if k['InstanceId'] == instance:
                stopInst = resource("ec2").instances.filter(InstanceIds=[self.instance]).start()
                print("Instance starting : %s " % self.instance)
            else:
                for status in resource("ec2").meta.client.describe_instance_status(InstanceIds=[self.instance])[
                    'InstanceStatuses']:
                    print(status['state-name-status'])


def getServers():
    import aws.envsetup.config
    import paramiko

    try:

        getServer = aws.envsetup.config.client("lightsail").get_instances()

        # print(yaml.dump(getServer))
        for server in getServer['instances']:
            ip = server['publicIpAddress']
            status = server['state']['name']

            if status == "running":
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.WarningPolicy)

                client.connect(ip, port=22, username="ubuntu", key_filename="/tmp/trustedted22111.pem")

                while True:
                    try:
                        cmd = input("#> ")
                        if cmd == "exit":
                            break
                        stdin, stdout, stderr = client.exec_command(cmd)
                        print(stdout.read().decode())
                    except KeyboardInterrupt as e:
                        break
                client.close()
    except ClientError as e:
        logger.warn(e)
        return False
    return True


def copy_file(keyfile, ip, sourcePath, destPath, port):
    from paramiko.sftp_client import SFTPClient
    import paramiko

    Client = paramiko.SSHClient()
    # Client.load_system_host_keys(keyfile)
    Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("[+] Connecting to hostname: %s" % ip)
    pk = paramiko.RSAKey.from_private_key(open(keyfile))

    conn = paramiko.Transport((ip, port))

    conn.connect(username="ubuntu", pkey=pk)

    sftp = SFTPClient.from_transport(conn)
    print("[+] Copying %s to %s" % (sourcePath, destPath))
    sftp.put(sourcePath, destPath)
    sftp.close()
    conn.close()


import string
from random import choice
import makepass


def generate_random_names(length=8, chars=string.digits):
    """Credit to Devin Leung"""
    return ''.join([choice(chars) for i in range(length)])


def vpn_server_names() -> object:
    for i in range(1):
        print("vpn_server_" + generate_random_names(4))


from aws.Themes.text import *


def Agreements():
    consent = "FUCKOFF"  # display(Fore.RED + menu_agreement)

    agreementPolicies = input("Enter (Y|y|N|n): ")
    if agreementPolicies == "Y" or agreementPolicies == "y":
        print("good to go")
        exit(1)
    elif agreementPolicies == "N" or agreementPolicies == "n":
        print(Fore.WHITE + "THANK YOU FOR USING LEFTSIDE.VISION")
        exit(0)

    else:
        print("Enter the write OPTIONS PLEASE .....")
        Agreements()

    return True


def sessionFileProbe():
    aws_id = input("Enter AWS ID: ")
    aws_secret = input("Enter AWS SecretKey: ")
    regional = input("Enter Regional Zone(us-west2|us-east-1): ")

    try:
        if os.path.exists("aws_configure_file.ini"):
            print("[+] Config File created Already....")
            pass
        else:
            with open("aws_configure_file.ini", "wt") as session_file:
                session_file.write(
                    "; config.ini\n ; AWS Configuration file\n\n [ default ] \n aws_access_key_id = %s \n aws_secret_access_key = %s \n regional_zone = %s" % (
                    aws_id, aws_secret, regional))
                session_file.close()
    except IOError as e:
        logger.error(e)
        return False
    return True


def AgreementsCheckFile():
    try:
        if not os.path.exists("agreement.txt"):
            with open("agreement.txt", "wt") as agree_file:
                agree_file.write("; YES TO AGREEMENT")
                agree_file.close()

        else:
            # print("[+] Agreement File created Already....")
            pass

    except IOError as e:
        logger.error(e)
        return False
    return True


def configurations():
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read('aws_configure_file.ini')
    sections = cfg.sections()
    aws_id = cfg.get('default', 'aws_access_key_id')
    aws_secret = cfg.get('default', 'aws_secret_access_key')
    region_zone = cfg.get('default', 'regional_zone')
    print(aws_id, aws_secret, region_zone)

# configurations()

# sessionFileProbe()
# AgreementsCheckFile()
# Agreements()
# getServers()
# grabInstances()
# copy_file("/tmp/VPN_TESTING_1.pem",
#		  "ec2-54-202-147-10.us-west-2.compute.amazonaws.com",
#		  "/home/elias777/PycharmProjects/Cloud9/aws/scripts/openvpn-install.sh",
#		  "/tmp/openvpn-install.sh", 22)
# publicIpAddress
# test_createInstance()
# IAM_USER.create_iam_user("ronin1")
# IAM_USER.delete_iam_user("ronin1")
# IAM_USER.create_key("ronin1")
# create_loginProfile("drumer1", "wanted1")
# IAM_USER.delete_key("huduee")
# IAM_USER.getKeys("ronin1", 20)
# IAM_USER.getUsers(13)
# IAM_USER.getPolicy("aws")
# checkLogs("Bentley777")
# onInstance()
# create_sa("wrecker33", "wrecker33")
# list_sa()
# delete_sa(input("Enter the email of Service Account to be deleted: "))
# list_roles()
# create_saKey("wrecker33@leftside-48941.iam.gserviceaccount.com")
# create_buckets("codesoul2", "EUROPE-CENTRAL2")
# create_instance()
# check_instagramAPI()
# create_sa("wrecker33", "wrecker33")
# list_sa()
# delete_sa(input("Enter the email of Service Account to be deleted: "))
# list_roles()
# create_saKey("wrecker33@leftside-48941.iam.gserviceaccount.com")
# create_buckets("codesoul2", "EUROPE-CENTRAL2")
# create_instance()
# check_instagramAPI()
# boat()
# delete_VPCID3()
# create_VPCID3()
# createSecurityGroup()
# keys101()
# keys102()
# createKeyPairs("tester6")
# createInstance()
# getKeys()
# deleteKeyPairs("eetdrumoro")
# createKeyPairs("tester55")
# createInstance()
# checkkeys1("tester6")
# describeSecurityGroups()
# makeSecurityGroups("tester6")
# vpcCreation()
# createInstance()
# getInstances()
# stop_Instances("i-037cda0f0391a2440")
# start_Instances("i-037cda0f0391a2440")
# stop_Instances("i-037cda0f0391a2440")
# start_Instances("i-037cda0f0391a2440")
# aws_list_buckets()
# aws_create_bucket("tester13390")
# aws_delete_bucket("kanada11")
# send_message("tester88393")
# getAcl()
# downloadAws("tester3390", "Ydl_links.txt", "/home/xza1/Downloads/Ydl_links.txt")
# upload_object("/home/xza1/Documents/CV/linux1_A.pdf", "kanada11", "linux1_A.pdf")
# testExists("tester1339099")
