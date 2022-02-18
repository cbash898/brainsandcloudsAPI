from aws.services.iam.iam_menu import *
from aws.services.ec2.ec2_menu import *
from aws.services.s3.s3 import *
from aws.services.lightsail.lightsail_menu import *
from aws.services.kms.kms import *
from aws.services.s3.s3_menu import *


def kmsMenu():
    shell("clear")
    banners("kms")
    display(SUB_KMS_MENU)
    CC = input(main_menu_text[0])

    # Picking the options
    if CC == "1":
        KMS.createMasterKey(choices(KMS_TEXTS[0]),
                            choices(KMS_TEXTS[1]))


    elif CC == "2":
        KMS.listCustomerMasterKey(choices(KMS_TEXTS[4]))


    elif CC == "3":
        KMS.listCustomerMasterKey(choices(KMS_TEXTS[3]))
        KMS.generateDataCrypto(choices(KMS_TEXTS[2]))

    elif CC == "4":
        KMS.listCustomerMasterKey(choices(KMS_TEXTS[3]))
        KMS.decryptDataCrypto(choices(KMS_TEXTS[2]))


    elif CC == "5":
        KMS.updateRegion(choices(KMS_TEXTS[2]),
                         choices(KMS_TEXTS[5]))

    elif CC == "6":
        KMS.deleteCustomKey(choices(KMS_TEXTS[2]),
                            choices(KMS_TEXTS[7]))

    elif CC == "7":
        KMS.listCustomerMasterKey(choices(KMS_TEXTS[3]))
        KMS.enableKeys(choices(KMS_TEXTS[2]))


    elif CC == "8":
        KMS.listCustomerMasterKey(choices(KMS_TEXTS[3]))
        KMS.disableKeys(choices(KMS_TEXTS[2]))



    elif CC == "9":
        KMS.encryptFile(choices(KMS_CRYPTOGRAPHY[0]),
                        choices(KMS_TEXTS[2]))

    elif CC == "10":
        KMS.decryptFile(choices(KMS_CRYPTOGRAPHY[0]))


    elif CC == "B" or CC == "b":
        main.main_menu()

    else:
        print(text_error)
        kmsMenu()

    return CC

