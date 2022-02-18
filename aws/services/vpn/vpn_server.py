import paramiko
from time import sleep
from aws.services.ec2.instances import *
from aws.Themes.text import *
from aws.envsetup.config import *




class VPNServer:


	def __init__(self):

		self.vpn_automated()



	@staticmethod
	def vpn_server_locations():

		display(vpnLocations)

		zone = input("Enter the Geography Zone: ")

		for i in vpnLocations:
			if i == zone:
				options = zone[i]
			return True


	@staticmethod
	def vpn_automated(
			keyname,
			groupname="automated_groupname",
			cidr="10.0.0.0/24",
			description="Automated Servers",
			ipProtocol="tcp",
			instance_type="t2.micro",
			zones='us-west-2a',
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

				print("Remember to save your KEYPAIR (/tmp/) .....")
				sleep(3)


		except exceptions.ClientError as e:

			if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
				logger.warning(' Duplicate Key Error (InvalidKeyPair)...')
			else:
				raise e

		server = client("ec2").run_instances(
			DryRun=False,
			ImageId=ImageIdUbuntu[0],
			MinCount=1,
			MaxCount=int(1),
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

			instanceIP = instance['PublicDnsName']
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

			# Hold done till server is in running state
			if True:

				connect_resource = resource("ec2")
				instance_work = connect_resource.Instance(id=instanceId)

				sleep(3)

				instance_work.wait_until_running(
					Filters=[
						{
							'Name': 'instance-state-name',
							'Values': [
								'running',
							]
						},
					],

			)

			#VPNServer.copy_file("/tmp/adb.1000.log",
			#		  instanceIP,
			#		  "/home/elias777/PycharmProjects/Cloud9/aws/scripts/openvpn-install.sh",
			#		  "/tmp/openvpn-install.sh", 22)

			#cmd_vpn2 = "cat /proc/cpuinfo"
			#cmd_vpn = "AUTO_INSTALL=y ./openvpn-install.sh"

			#VPNServer.run_command(instanceIP, 22, "ubuntu", keyFile, cmd_vpn2)


	@staticmethod
	def copy_file(keyfile, ip, sourcePath, destPath, port):

		from paramiko.sftp_client import SFTPClient
		import paramiko

		Client = paramiko.SSHClient()
		#Client.load_system_host_keys(keyfile)
		Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		print("[+] Connecting to hostname: %s" % ip)

		conn = paramiko.Transport((ip, port))

		print("[+] Copying %s to %s" % (sourcePath, destPath))
		conn.connect(username="ubuntu", pkey=keyfile)

		sftp = SFTPClient.from_transport(conn)

		sftp.put(sourcePath, destPath)
		sftp.close()
		conn.close()


	def download_file(keyfile, ip, sourcePath, destPath, port):

		from paramiko.sftp_client import SFTPClient
		import paramiko

		Client = paramiko.SSHClient()
		#Client.load_system_host_keys(keyfile)
		Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		print("[+] Connecting to hostname: %s" % ip)

		conn = paramiko.Transport((ip, port))

		print("[+] Copying %s to %s" % (sourcePath, destPath))
		conn.connect(username="ubuntu", pkey=keyfile)

		sftp = SFTPClient.from_transport(conn)

		sftp.get(sourcePath, destPath)
		sftp.close()
		conn.close()


	@staticmethod
	def run_command(ip, port, username, keyfile, cmd):

		connbeef = paramiko.SSHClient()
		#connbeef.load_system_host_keys()
		connbeef.set_missing_host_key_policy(paramiko.WarningPolicy)

		connbeef.connect(ip, port, username, key_filename=keyfile)

		stdin, stdout, stderr = connbeef.exec_command(cmd)
		print(stdout.read().decode())

		connbeef.close()



