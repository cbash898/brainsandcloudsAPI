from cryptography.fernet import Fernet, MultiFernet
import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


def encryptFile(datafile, encryptionType):

    try:

        with open(datafile, "rb") as f:
            file_contents = f.read()

            if encryptionType == "Asymmetric":

                key1 = Fernet(Fernet.generate_key())
                key2 = Fernet(Fernet.generate_key())
                f = MultiFernet([key1, key2])
                token = f.encrypt(file_contents)

                with open(datafile + "_encrypted", "wb") as encrypted_file:

                    encrypted_file.write(token)
                    encrypted_file.close()

            elif encryptionType == "Symmetric":

                key1 = Fernet.generate_key()

                #with open(keyFile, "rt") as kf:
                #	print(key1, file=kf)
                #	kf.close()

                f = Fernet(key1)
                token = f.encrypt(file_contents)

                with open(datafile + "_encrypted", "wb") as encrypted_file:
                    encrypted_file.write(token)
                    encrypted_file.close()

    except IOError as e:
        logger.error(e)
        return None
