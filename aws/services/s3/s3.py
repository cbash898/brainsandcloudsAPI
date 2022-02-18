import logging
import os
import time
import yaml
from botocore import exceptions
from aws.envsetup.config import *
from aws.Themes.text import *
import base64
from cryptography.fernet import Fernet

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


class KMS:

    def __init__(self):
        pass

    @staticmethod
    def createMasterKey(keyname, Desc):

        aliasName = "alias/" + keyname
        try:

            createCMK = client("kms").create_key(

                Description=Desc,
                # KeyUsage='ENCRYPT_DECRYPT',
                # CustomerMasterKeySpec=cmkSpec,
                # Origin=origin,
                # CustomKeyStoreId='string',
                BypassPolicyLockoutSafetyCheck=False,
                # MultiRegion=False
            )

            getAlias = client("kms").create_alias(AliasName=aliasName, TargetKeyId=createCMK['KeyMetadata']['KeyId'])

            print(yaml.dump(createCMK))

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

    @staticmethod
    def listCustomerMasterKey(limit):

        try:

            listKeys = client("kms").list_keys(
                Limit=int(limit),
            )

            for keys in listKeys['Keys']:
                describe = client("kms").describe_key(KeyId=keys['KeyId'])

                print(yaml.dump(describe['KeyMetadata']))

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

    @staticmethod
    def generateDataCrypto(keyId):

        try:

            singleCrypto = client("kms").generate_data_key(
                KeyId=keyId,
                KeySpec='AES_256',
            )

            print(yaml.dump(singleCrypto))

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

        return singleCrypto['CiphertextBlob'], base64.b64encode(singleCrypto['Plaintext'])

    @staticmethod
    def decryptDataCrypto(encrypted_data_key):

        try:

            multiCrypto = client("kms").decrypt(
                CiphertextBlob=encrypted_data_key
            )

            print(yaml.dump(multiCrypto))

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

        return base64.b64encode(multiCrypto['Plaintext'])

    @staticmethod
    def updateRegion(keyID, region):

        try:

            region = client("kms").update_primary_region(
                KeyId=keyID,
                PrimaryRegion=region
            )
            print(yaml.dump(region))

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

    @staticmethod
    def enableKeys(self):

        try:

            enabled = client("kms").enable_key(KeyId=self)
            print(yaml.dump(enabled))

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

    @staticmethod
    def disableKeys(self):

        try:

            disabled = client("kms").disable_key(KeyId=self)
            print(yaml.dump(disabled))

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

    def deleteCustomKey(self, days):

        try:
            response = client("kms").schedule_key_deletion(
                KeyId=self,
                PendingWindowInDays=int(days)
            )
            print(response)

        except exceptions.ClientError as e:
            logger.error(e)
            return None, None

    @staticmethod
    def encryptFile(datafile, keyId):

        """Reference to aws.amazon.com
        https://boto3.amazonaws.com/v1/documentation/api/latest/guide/kms-example-encrypt-decrypt-file.html
        number of Bytes for Len = 256
        """
        NUM_OF_BYTES = 256
        try:

            with open(datafile, "rb") as f:
                file_contents = f.read()

        except IOError as e:
            logger.error(e)
            return False

        data_key, plaintext = KMS.generateDataCrypto(keyId)

        if data_key is None:
            return False
        logger.error("Creating New DataKey")

        f = Fernet(plaintext)
        files_encrypting = f.encrypt(file_contents)

        try:
            with open(datafile + "_encrypted", "wb") as file_encrypted:
                file_encrypted.write(len(data_key).to_bytes(NUM_OF_BYTES, byteorder="big"))

                file_encrypted.write(data_key)
                file_encrypted.write(files_encrypting)
        except IOError as e:
            logger.error(e)
            return False

        return True

    @staticmethod
    def decryptFile(datafile_encrypted):

        """Reference to aws.amazon.com
                https://boto3.amazonaws.com/v1/documentation/api/latest/guide/kms-example-encrypt-decrypt-file.html
                number of Bytes for Len = 256
                """
        NUM_OF_BYTES = 256
        try:

            with open(datafile_encrypted, "rb") as fd:
                file_contents = fd.read()

        except IOError as e:
            logger.error(e)
            return False

        data_key_file_len = int.from_bytes(file_contents[:NUM_OF_BYTES], byteorder='big') + NUM_OF_BYTES

        encrypted_data_key = file_contents[NUM_OF_BYTES:data_key_file_len]

        plaintext_data = KMS.decryptDataCrypto(encrypted_data_key)
        if plaintext_data is None:
            return False

        f = Fernet(plaintext_data)
        file_contents = f.decrypt(file_contents[data_key_file_len:])

        try:
            with open(datafile_encrypted + "_decrypted", "wb") as file_contents_decrypted:
                file_contents_decrypted.write(file_contents)

        except IOError as e:
            logger.error(e)
            return False
        return True




