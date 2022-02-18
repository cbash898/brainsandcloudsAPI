import logging
import yaml
from botocore import exceptions
from aws.envsetup.config import *
from aws.scripts.pen_scripts import *

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()



class EC2:

	def __init__(self):
		self.cidr = "10.0.0.1/24"

	@staticmethod
	def getKeysPairs():

		getKeyInfos = client("ec2").describe_key_pairs()

		for key in getKeyInfos['KeyPairs']:
			print("\nKeyName: {}".format(key['KeyName']),
				  "\nKeyPairId: {}".format(key['KeyPairId']),
				  "\nKeyFingerprint: {}".format(key['KeyFingerprint'])
				  )


	@staticmethod
	def createKeyPairs(self):

		# KeyFIles
		keyDir = "/tmp/"
		keyFileFormat = ".pem"
		keyFile = keyDir + self + keyFileFormat

		EC2.getKeysPairs()

		try:

			keysCreation = client("ec2").create_key_pair(KeyName=self)
			print("\n[+] Creating KeyPair for %s" % self)
			private_key = keysCreation['KeyMaterial']
			# Props to learnaws.org
			with os.fdopen(os.open(keyFile, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as e:
				e.write(private_key)


		except exceptions.ClientError as e:

			if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
				logger.warning(' Duplicate Key Error (InvalidKeyPair)...')
			else:
				raise e



	def deleteKeyPairs(self):


		EC2.getKeysPairs()
		try:

			deleteKey = client("ec2").delete_key_pair(KeyName=self)

		except exceptions.ClientError as e:
			if e.response['Error']['Code'] == "InvalidKeyPair.NotFound":
				logger.warning("NonExisting Keyname: %s" % self)

			else:
				raise e


	def updateKeyPairs(self):


		EC2.getKeysPairs()
		try:

			deleteKey = client("ec2").update_key_pair(KeyName=self)

		except exceptions.ClientError as e:
			if e.response['Error']['Code'] == "InvalidKeyPair.NotFound":
				logger.warning("NonExisting Keyname: %s" % self)

			else:
				raise e



	@staticmethod
	def getInstances():

		request = client("ec2").describe_instances()

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


	def stop_Instance(self):

		EC2.getInstances()
		# instance = input("\nEnter the id of instance to be stopped: ")

		request = client("ec2").describe_instances()

		for i in request['Reservations']:
			for k in i['Instances']:
				if k['InstanceId'] == self:
					stopInst = resource("ec2").instances.filter(InstanceIds=[self]).stop()
					time.sleep(7)
					print("Instance stopping : %s " % self)
				else:
					for status in resource("ec2").meta.client.describe_instance_status(InstanceIds=[self])['InstanceStatuses']:
						print(status['InstanceState'])


	def start_Instances(self):

		EC2.getInstances()

		request = client("ec2").describe_instances()

		for i in request['Reservations']:
			for k in i['Instances']:
				if k['InstanceId'] == self:
					stopInst = resource("ec2").instances.filter(InstanceIds=[self]).start()
					time.sleep(7)
					print("Instance starting : %s " % self)
				else:
					for status in resource("ec2").meta.client.describe_instance_status(InstanceIds=[self])['InstanceStatuses']:
						print(status['InstanceState'])


	def deleteInstance(self):

		EC2.getInstances()

		request = client("ec2").describe_instances()

		for i in request['Reservations']:
			for k in i['Instances']:
				if k['InstanceId'] == self:
					stopInst = resource("ec2").instances.filter(InstanceIds=[self]).terminate()
					time.sleep(7)
					print("Instance Terminated: %s " % self)
				else:
					for status in resource("ec2").meta.client.describe_instance_status(InstanceIds=[self])[
						'InstanceStatuses']:
						print(status['InstanceState'])





	@staticmethod
	def createInstance(
			keyname,
			groupname,
			cidr,
			description,
			ipProtocol,
			instance_type,
			zones,
			volumeSize,
			volumeType
	):

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
																   Description=description,
																   VpcId=get_vpc.id)

				response = client("ec2").authorize_egress(
					DryRun=False,
					SourceSecurityGroupName=groupname,
					SourceSecurityGroupOwnerId=securityGroupCreation['GroupId'],
					IpProtocol=ipProtocol,
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

			UserData=pentest,
			InstanceType=instance_type,

			Placement={
				'AvailabilityZone': zones,
				'Tenancy': 'default'
			},

			BlockDeviceMappings=[
				{
					'VirtualName': 'string',
					'DeviceName': '/dev/sdh',
					'Ebs': {
						'VolumeSize': int(volumeSize),
						'DeleteOnTermination': True,
						'VolumeType': volumeType,
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



	def elasticIP(self):
		pass

	def networkInterfaces(self):
		pass

	def createVPC(self):
		return self.vpc



	def deleteSecurityGroups(self):

		EC2.getSecurityGroup()
		try:
			securityGroupDelete = client("ec2").delete(DryRun=False, GroupNames=self)
			EC2.getSecurityGroup()

		except exceptions.ClientError as e:

			if e.response['Error']['Code'] == "InvalidGroup.NotFound":
				print("[+] %s security group NotFound %s" % self)
			else:
				raise



	@staticmethod
	def getSecurityGroup():

		try:

			get_group = client("ec2").describe_security_groups()
			print(yaml.dump(get_group))
		except exceptions.ClientError as e:
			logger.warning("Error: ")
		pass




	def create_security_groups(self, desc, cidr="10.0.0.0/24"):


		try:

			request = client("ec2").describe_security_groups(GroupNames=[self])

		except exceptions.ClientError as e:

			if e.response['Error']['Code'] == "InvalidGroup.NotFound":
				print("[+] Creating security group for %s" % self)
				get_vpc = client("ec2").create_vpc(CidrBlock=cidr)
				securityGroupCreation = get_vpc.create_security_group(DryRun=False, GroupNames=self,
																	  Description=desc)

				response = client("ec2").authorize_egress(
					DryRun=False,
					SourceSecurityGroupName=self,
					SourceSecurityGroupOwnerId=securityGroupCreation['GroupId'],
					IpProtocol='tcp',
					FromPort=22,
					ToPort=22,
					CidrIp=cidr)

			else:
				raise




class EC2_AUTOMATION:

	def __init__(self):
		pass

	@staticmethod
	def automated_instances(self,
			keyname="automated_server1",
			groupname="automated_groupname",
			cidr="10.0.0.0/24",
			description="Automated Servers",
			ipProtocol="tcp",
			instance_type="t2.medium",
			zones="us-west-2a",
			volumeSize=50,
			volumeType="standard"
	):

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
																			 Description=description,
																			 VpcId=get_vpc.id)

				response = client("ec2").authorize_egress(
					DryRun=False,
					SourceSecurityGroupName=groupname,
					SourceSecurityGroupOwnerId=securityGroupCreation['GroupId'],
					IpProtocol=ipProtocol,
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
			MaxCount=int(self),
			KeyName=keyname,

			UserData=pentest,
			InstanceType=instance_type,

			Placement={
				'AvailabilityZone': zones,
				'Tenancy': 'default'
			},

			BlockDeviceMappings=[
				{
					'VirtualName': 'string',
					'DeviceName': '/dev/sdh',
					'Ebs': {
						'VolumeSize': int(volumeSize),
						'DeleteOnTermination': True,
						'VolumeType': volumeType,
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
