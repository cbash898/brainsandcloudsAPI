import logging
import yaml
from botocore import exceptions
from aws.envsetup.config import *
from aws.scripts.pen_scripts import *
import paramiko

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


class LightSail:

    def __init__(self):
        pass

    @staticmethod
    def getKeysPairs():

        getKeyInfos = client("lightsail").get_key_pairs()

        print(yaml.dump(getKeyInfos))

    @staticmethod
    def createKeyPairs(self):

        # KeyFIles
        keyDir = "/tmp/"
        keyFileFormat = ".pem"
        keyFile = keyDir + self + keyFileFormat

        LightSail.getKeysPairs()

        try:

            keysCreation = client("lightsail").create_key_pair(
                keyPairName=self,
                tags=[
                    {
                        'key': 'Project',
                        'value': 'Blob'
                    },
                ]

            )
            print("\n[+] Creating KeyPair for %s" % self)
            private_key = keysCreation['']
            # Props to learnaws.org
            with os.fdopen(os.open(keyFile, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as e:
                e.write(private_key)

        except exceptions.ClientError as e:

            if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
                logger.warning(' Duplicate Key Error (InvalidKeyPair)...')
            else:
                raise e

    def deleteKeyPairs(self):

        LightSail.getKeysPairs()
        try:

            deleteKey = client("lightsail").delete_key_pair(

                keyPairName=self)

            print(yaml.dump(deleteKey))

        except exceptions.ClientError as e:
            if e.response['Error']['Code'] == "InvalidKeyPair.NotFound":
                logger.warning("NonExisting Keyname: %s" % self)

            else:
                raise e

    @staticmethod
    def getServers():

        try:

            getServer = client("lightsail").get_instances()

            print(yaml.dump(getServer))

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    @staticmethod
    def logIntoServers(keyfile):

        try:

            getServer = client("lightsail").get_instances()

            # print(yaml.dump(getServer))
            for server in getServer['instances']:
                ip = server['publicIpAddress']
                status = server['state']['name']

                if status == "running":
                    connbeef = paramiko.SSHClient()
                    connbeef.load_system_host_keys()
                    connbeef.set_missing_host_key_policy(paramiko.WarningPolicy)

                    connbeef.connect(ip, port=22, username="ubuntu", key_filename=keyfile)

                    while True:
                        try:
                            cmd = input("#> ")
                            if cmd == "exit":
                                break
                            stdin, stdout, stderr = connbeef.exec_command(cmd)
                            print(stdout.read().decode())
                        except KeyboardInterrupt as e:
                            break
                    connbeef.close()
        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    @staticmethod
    def startServer(self):

        LightSail.getServers()
        # instance = input("\nEnter the id of instance to be stopped: ")

        try:

            start = client("lightsail").start_instance(instanceName=self, force=True)
            print(yaml.dump(start))

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    def stopServer(self):

        LightSail.getServers()
        # instance = input("\nEnter the id of instance to be stopped: ")

        try:

            stop = client("lightsail").stop_instance(instanceName=self, force=True)
            print(yaml.dump(stop))

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    def deleteServer(self):

        LightSail.getServers()
        # instance = input("\nEnter the id of instance to be stopped: ")

        try:

            delete = client("lightsail").delete_instance(instanceName=self, forceDeleteAddOns=True)
            print(yaml.dump(delete))

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    @staticmethod
    def createServer(self, keyname):

        # KeyFiles
        keyDir = "/tmp/"
        keyFileFormat = ".pem"
        keyFile = keyDir + keyname + keyFileFormat

        try:

            keysCreation = client("lightsail").create_key_pair(keyPairName=keyname)
            print("\n[+] Creating KeyPair for %s" % keyname)
            private_key = keysCreation['privateKeyBase64']
            # Props to learnaws.org
            with os.fdopen(os.open(keyFile, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as e:
                e.write(private_key)

        except exceptions.ClientError as e:

            if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
                logger.warning(' Duplicate Key Error (InvalidKeyPair)...')
            else:
                raise e

        try:

            server = client("lightsail").create_instances(
                instanceNames=[
                    self,
                ],
                availabilityZone='us-west-2a',
                blueprintId='ubuntu_20_04',
                bundleId='micro_2_0',
                userData=pentest,
                keyPairName=keyname,
                tags=[
                    {
                        'key': 'Project',
                        'value': 'Blog'
                    },
                ],
                addOns=[
                    {
                        'addOnType': 'AutoSnapshot',
                        'autoSnapshotAddOnRequest': {
                            'snapshotTimeOfDay': '02:00'
                        }
                    },
                ],
                ipAddressType='ipv4'
            )

            time.sleep(35)

            for instance in server['instances']:
                ip = instance['publicIpAddress']
                status = instance['state']['name']

                time.sleep(10)
                if status == "running":

                    connbeef = paramiko.SSHClient()
                    connbeef.load_system_host_keys()
                    connbeef.set_missing_host_key_policy(paramiko.WarningPolicy)

                    connbeef.connect(ip, port=22, username="ubuntu", key_filename=keyFile)

                    while True:
                        try:
                            cmd = input("#> ")
                            if cmd == "exit":
                                break
                            stdin, stdout, stderr = connbeef.exec_command(cmd)
                            print(stdout.read().decode())
                        except KeyboardInterrupt as e:
                            logger.warn(e)
                            break
                    connbeef.close()

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True


    @staticmethod
    def getPorts(serverName):

        try:

            portState = client("lightsail").get_instance_port_states(
                instanceName=serverName
            )
            print(yaml.dump(portState))

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    @staticmethod
    def openPorts(serverName, serverIP, port):

        try:
            portNumber = client("lightsail").open_instance_public_ports(
                portInfo={
                    'fromPort': port,
                    'toPort': port,
                    'protocol': 'tcp',
                    'cidrs': [
                        serverIP,
                    ],
                    'cidrListAliases': [
                        'string',
                    ]
                },
                instanceName=serverName
            )

            print(yaml.dump(portNumber))

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    def grab_snapshots(self):

        try:
            gsnapShot = client('lightsail').get_disks_snapshot(instanceSnapshotName=self)
            print(yaml.dump(gsnapShot))
        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    def exports_snapshots(self):

        try:
            exsnapShots = client('lightsail').export_snapshot(Name=self)
            print(yaml.dump(exsnapShots))
        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    def make_snapshots(self, instance):

        try:
            makeSnaps = client('lightsail').create_instance_snapshot(instanceSnapshotName=self, instanceName=instance)
            print(yaml.dump(makeSnaps))
        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True
    
    def remove_snapshots(self):

        try:
            remove_snapShot = client('lightsail').delete_snapshot(instanceSnapshotName=self)
            print(yaml.dump(remove_snapShot))
        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    def grabbing_staticIp(self):

        try:
            grap_static = client('lightsail').get_static_ip(staticIpName=self)
            print(yaml.dump(grap_static))
        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True

    def connect_staticIp(self):

        try:
            staticIp_connect = client('lightsail').attach_static_ip(staticIpName=self)
            print(yaml.dump(staticIp_connect))
        except exceptions as e:
            logger.warn(e)
            return False
        return True

    def disconnect_staticIp(self):

        try:
            staticIp_disconnect = client('lightsail').detach_static_ip(staticIpName=self)
            print(yaml.dump(staticIp_disconnect))
        except exceptions as e:
            logger.warn(e)
            return False
        return True


class LIGHTSAIL_AUTOMATION:

    def __init__(self):
        pass

    @staticmethod
    def automatedServer(self, keyname):

        # KeyFiles
        keyDir = "/tmp/"
        keyFileFormat = ".pem"
        keyFile = keyDir + keyname + keyFileFormat

        try:

            keysCreation = client("lightsail").create_key_pair(keyPairName=keyname)
            print("\n[+] Creating KeyPair for %s" % keyname)
            private_key = keysCreation['privateKeyBase64']
            # Props to learnaws.org
            with os.fdopen(os.open(keyFile, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as e:
                e.write(private_key)

        except exceptions.ClientError as e:

            if e.response['Error']['Code'] == "InvalidKeyPair.Duplicate":
                logger.warning(' Duplicate Key Error (InvalidKeyPair)...')
            else:
                raise e

        try:
            serverInstance = client("lightsail").create_instances(
                instanceNames=[
                    self,
                ],
                availabilityZone='us-west-2a',
                blueprintId='ubuntu_18_04',
                bundleId='micro_2_0',
                userData=pentest,
                keyPairName=keyname,
                tags=[
                    {
                        'key': 'Project',
                        'value': 'Blog'
                    },
                ],
                addOns=[
                    {
                        'addOnType': 'AutoSnapshot',
                        'autoSnapshotAddOnRequest': {
                            'snapshotTimeOfDay': '02:00'
                        }
                    },
                ],
                ipAddressType='ipv4'
            )

            for instance in serverInstance['instances']:
                ip = instance['publicIpAddress']
                status = instance['state']['name']

                if status == "running":
                    connbeef = paramiko.SSHClient()
                    connbeef.load_system_host_keys()
                    connbeef.set_missing_host_key_policy(paramiko.WarningPolicy)

                    connbeef.connect(ip, port=22, username="ubuntu", key_filename=keyFile)

                    while True:
                        try:
                            cmd = input("#> ")
                            if cmd == "exit":
                                break
                            stdin, stdout, stderr = connbeef.exec_command(cmd)
                            print(stdout.read().decode())
                        except KeyboardInterrupt as e:
                            logger.warn(e)
                            break
                    connbeef.close()

                print(yaml.dump(serverInstance))

        except exceptions.ClientError as e:
            logger.warn(e)
            return False
        return True
