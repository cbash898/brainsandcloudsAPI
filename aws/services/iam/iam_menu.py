import main
from aws.services.kms.kms_menu import *
from aws.services.iam.identity_manager import *
from aws.Themes.text import *
from aws.Themes.styles import *
from aws.Themes.images import *
from colorama import Fore
from time import sleep
from aws.envsetup.config import *
from aws.services.ec2.ec2_menu import *


def iam_menu():
    banners("iam")
    display(IAM_MENU)
    CC = input(main_menu_text[0])

    # Picking the options
    if CC == "1":
        sub_iam_user_menu()
    elif CC == "2":
        sub_iam_keypairs_menu()
    elif CC == "3":
        sub_iam_policy_menu()
    elif CC == "4":
        sub_iam_loginProfile_menu()

    elif CC == "B" or CC == "b":
        main.main_menu()
    else:
        print(text_error)
        iam_menu()


def sub_iam_user_menu():

    shell("clear")
    banners("iam")
    display(SUB_IAM_MENU)
    CC = input(ec2_text_instance[0])

    # Pick Options
    if CC == "1":
        CC = IAM_USER.create_iam_user(choices("Enter Username: "))
        sleep(2)
        sub_iam_user_menu()

    elif CC == "2":
        CC = IAM_USER.getUsers()
        sleep(2)
        sub_iam_user_menu()

    elif CC == "3":
        CC = IAM_USER.update_iam_user(choices("Enter Old Username: "), choices("Enter NewUser"))
        sleep(2)
        sub_iam_user_menu()

    elif CC == "4":
        CC = IAM_USER.delete_iam_user(choices("Enter Username: "))
        sleep(2)
        sub_iam_user_menu()

    elif CC == "B" or CC == "b":
        main.iam_menu()
    else:
        print(text_error)
        sub_iam_user_menu()
    return CC


def sub_iam_keypairs_menu():

    shell("clear")
    banners("iam")
    display(SUB_IAM_KEYPAIRS_MENU)
    CC = input(ec2_text_instance[0])

# Pick Options
    if CC == "1":
        CC = IAM_KEYS.getKeys(choices(iam_text_user[0]), choices("Enter MaxItems: "))
        sleep(2)
        sub_iam_keypairs_menu()

    elif CC == "2":
        CC = IAM_KEYS.create_key(choices(iam_text_user[0]))
        sleep(2)
        sub_iam_keypairs_menu()

    elif CC == "3":
        CC = IAM_KEYS.delete_key(choices(iam_text_user[0]), choices("Enter AccessId: "))
        sleep(2)
        sub_iam_keypairs_menu()

    elif CC == "B" or CC == "b":
        main.iam_menu()
    else:
        print(text_error)
        sub_iam_keypairs_menu()
    return CC


# Create the iam Policy Menu()
def sub_iam_policy_menu():

    shell("clear")
    banners("iam")
    display(SUB_IAM_POLICY_MENU)
    CC = input(ec2_text_instance[0])

    # Pick Options
    if CC == "1":
        CC = IAM_POLICY.getPolicy(choices("Enter Policy Type: (All|Local|AWS): "), choices("Enter MaxItem to display: "))
        sleep(3)
        sub_iam_policy_menu()


    elif CC == "2":
        CC = IAM_POLICY.attach_policy(choices("Enter ARN: "), choices("Enter RoleName"))
        sleep(3)
        sub_iam_policy_menu()


    elif CC == "3":
        CC = IAM_POLICY.detach_policy(choices("Enter ARN: "), choices("Enter RoleName: "))
        sleep(3)
        sub_iam_policy_menu()

    elif CC == "B" or CC == "b":
         main.main_menu()

    else:
        print(text_error)
        sub_iam_policy_menu()
    return CC



def sub_iam_loginProfile_menu():

    shell("clear")
    banners("iam")
    display(SUB_IAM_LOGINPROFILE_MENU)
    CC = input(ec2_text_instance[0])

    # Pick Options
    if CC == "1":
        CC = LoginUser.create_loginProfile(choices(iam_text_user[0]), choices("Enter password: "))
        sleep(3)
        sub_iam_loginProfile_menu()

    elif CC == "2":
        CC = LoginUser.checkLoginProfile(choices(iam_text_user))

    elif CC == "3":
        CC = LoginUser.deleteLoginProfile(choices(iam_text_user))

    elif CC == "B" or CC == "b":
        main.iam_menu()
    else:
        print(text_error)
        sub_iam_loginProfile_menu()
    return CC



