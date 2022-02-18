from aws.services.iam.iam_menu import *
from aws.services.ec2.instances import *
from aws.Themes.images import *
from aws.Themes.text import *
from aws.Themes.styles import *
from aws.services.s3.s3_menu import *
from aws.services.lightsail.lightsail_menu import *
from aws.services.kms.kms_menu import *
from aws.services.route53.route53_menu import *
from aws.envsetup.config import *
from aws.services.vpn.vpn_server import VPNServer


def ec2Menu():
    shell("clear")
    banners("ec2")
    display(EC2_MENU)
    CC = input(main_menu_text[0])

    # Picking the options
    if CC == "1":
        ec2_instanceMenu()

    elif CC == "2":
        ec2_KeyPairMenu()

    elif CC == "3":
        ec2_SecurityGroupMenu()

    elif CC == "4":
        ec2_NetworkACLMenu()

    elif CC == "5":
        ec2_Automated()
        sleep(3)
        ec2Menu()

    elif CC == "6":
        VPNServer.vpn_automated(choices(vpn_server_names()))
        sleep(3)
        ec2Menu()

    elif CC == "B" or CC == "b":
        main.main_menu()

    else:
        print(text_error)
        ec2Menu()



def ec2_instanceMenu():

    shell("clear")
    display(SUB_EC2_MENU)
    CC = input(main_menu_text[0])

    # Pick Options
    if CC == "1":
        CC = EC2.createInstance(choices(ec2_text_instance[0]),
                                choices(ec2_text_instance[1]),
                                choices(ec2_text_instance[2]),
                                choices(ec2_text_instance[3]),
                                choices(ec2_text_instance[4]),
                                choices(ec2_text_instance[6]),
                                choices(ec2_text_instance[7]),
                                choices(ec2_text_instance[8]),
                                choices(ec2_text_instance[9]))
        sleep(2)
        ec2_instanceMenu()

    elif CC == "2":
        CC = EC2.getInstances()
        sleep(2)
        ec2_instanceMenu()

    elif CC == "3":
        EC2.getInstances()
        CC = EC2.start_Instances(choices("\nEnter InstanceId: "))
        sleep(2)
        ec2_instanceMenu()

    elif CC == "4":
        EC2.getInstances()
        CC = EC2.stop_Instance(choices("\nEnter InstanceId: "))
        sleep(2)
        ec2_instanceMenu()


    elif CC == "5":
        EC2.getInstances()
        CC = EC2.deleteInstance(choices("\nEnter InstanceId: "))
        sleep(2)
        ec2_instanceMenu()

    elif CC == "B" or CC == "b":
        ec2Menu()

    else:
        print(text_error)
        ec2_instanceMenu()
    return CC


def ec2_KeyPairMenu():

    shell("clear")
    display(SUB_EC2_KEYPAIR_MENU)
    CC = input(main_menu_text[0])

# Pick Options
    if CC == "1":
        CC = EC2.getKeysPairs()
        sleep(2)
        ec2_KeyPairMenu()

    elif CC == "2":
        CC = EC2.createKeyPairs(choices(ec2_text_keys[0]))
        sleep(2)
        ec2_KeyPairMenu()

    elif CC == "3":
        CC = EC2.deleteKeyPairs(choices(ec2_text_keys[0]))
        sleep(2)
        ec2_KeyPairMenu()

    elif CC == "B" or CC == "b":
        ec2Menu()
    else:
        display(text_error)
        ec2_KeyPairMenu()
    return CC


# Create the iam Policy Menu()
def ec2_SecurityGroupMenu():
    shell("clear")
    display(SUB_EC2_SECURITYGROUP_MENU)
    CC = input(main_menu_text[0])

    # Pick Options
    if CC == "1":
        CC = EC2.getSecurityGroup()
        sleep(3)
        ec2_SecurityGroupMenu()


    elif CC == "2":
        EC2.getSecurityGroup()
        CC = EC2.create_security_groups(choices(ec2_text_keys[2]), choices(ec2_text_keys[3]))
        sleep(3)
        ec2_SecurityGroupMenu()


    elif CC == "3":
        EC2.getSecurityGroup()
        CC = EC2.deleteSecurityGroups(choices(ec2_text_keys[2]))
        sleep(3)
        ec2_SecurityGroupMenu()

    elif CC == "B" or CC == "b":
        ec2Menu()

    else:
        display(text_error)
        ec2_SecurityGroupMenu()
    return CC



def ec2_NetworkACLMenu():

    shell("clear")
    display(SUB_EC2_NETWORKACL_MENU)
    CC = input(main_menu_text[0])

    # Pick Options
    if CC == "1":
        CC = LoginUser.create_loginProfile(choices(iam_text_user[0]), choices("Enter password: "))
        sleep(3)
        ec2_NetworkACLMenu()

    elif CC == "2":
        CC = LoginUser.checkLoginProfile(choices(iam_text_user))
        sleep(2)
        ec2_NetworkACLMenu()

    elif CC == "3":
        CC = LoginUser.deleteLoginProfile(choices(iam_text_user))
        sleep(2)
        ec2_NetworkACLMenu()

    elif CC == "4":
        CC = LoginUser.deleteLoginProfile(choices(iam_text_user))
        sleep(2)
        ec2_NetworkACLMenu()


    elif CC == "B" or CC == "b":
        ec2Menu()

    else:
        display(text_error)
        ec2_NetworkACLMenu()
    return CC


def ec2_Automated():

    EC2_AUTOMATION.automated_instances(choices("Enter the Max Amount of Instances (int): "))

    return
