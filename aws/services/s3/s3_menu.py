import main
from aws.services.iam.iam_menu import *
from aws.services.ec2.ec2_menu import *
from aws.services.s3.s3 import *
from time import sleep
from aws.services.kms.kms_menu import *
from aws.services.lightsail.lightsail_menu import *
from aws.envsetup.config import *
from aws.Themes.text import *
from aws.Themes.styles import *
from aws.Themes.images import *


def s3Menu():

    shell("clear")
    banners("s3")
    display(S3_MENU)
    CC = input(main_menu_text[0])

    # Picking the options
    if CC == "1":
        s3BucketMenu()

    elif CC == "2":
        s3BucketWebsite()

    elif CC == "3":
        s3Encryption()


    elif CC == "B" or CC == "b":
        main.main_menu()

    else:
        print(text_error)
        s3Menu()

    return CC


def s3BucketMenu():

    display(SUB_S3_MENU)
    CC = input(main_menu_text[0])

    # Picking the options
    if CC == "1":
        s3Buckets.getbuckets()
        sleep(3)
        s3BucketMenu()


    elif CC == "2":
        s3Buckets.s3_create_bucket(choices(s3_text_words[0]))
        sleep(3)
        s3BucketMenu()


    elif CC == "3":
        s3Buckets.getbuckets()
        s3Buckets.uploadAWS(choices(s3_text_words[2]),
                            choices(s3_text_words[0]),
                            choices(s3_text_words[3]))
        sleep(3)
        s3BucketMenu()

    elif CC == "4":
        s3Buckets.getbuckets()
        s3Buckets.downloadAws(choices(s3_text_words[0]),
                              choices(s3_text_words[3]),
                              choices(s3_text_words[2]))
        sleep(5)
        s3BucketMenu()

    elif CC == "6":
        s3Buckets.s3_delete_objects(choices(s3_text_words[3]))
        sleep(5)
        s3BucketMenu()

    elif CC == "7":
        s3Buckets.getbuckets()
        s3Buckets.getAcl(choices(s3_text_words[0]))
        sleep(5)
        s3BucketMenu()


    elif CC == "8":
        s3Buckets.getbuckets()
        s3Buckets.s3_delete_bucket(choices(s3_text_words[0]))

        sleep(5)
        s3BucketMenu()

    elif CC == "B" or CC == "b":
        main.main_menu()

    else:
        print(text_error)
        s3Menu()

    return CC


def s3BucketWebsite():
    pass



def s3Encryption():
    pass
