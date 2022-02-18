from aws.envsetup.config import *
import random
from colorama import Fore
from aws.Themes.text import *
from aws.Themes.images import *


def logoColorization():

    logos = [
        (Fore.CYAN + realTime() + LEFTSIDE1),
        (Fore.GREEN + realTime() + LEFTSIDE2),
        (Fore.MAGENTA + realTime() + LEFTSIDE3),
        (Fore.YELLOW + realTime() + LEFTSIDE4),
        (Fore.RED + realTime() + LEFTSIDE5)
    ]

    logo = random.randrange(0, 4)

    if logo == 0:
        print(logos[0])
        return

    if logo == 1:
        print(logos[1])
        return

    if logo == 2:
        print(logos[2])
        return

    if logo == 3:
        print(logos[3])
        return

    if logo == 4:
        print(logos[4])




def banners(self):


    services = ["iam", "ec2", "s3", "lightsail", "route53", "kms"]
    #random the colors
    services_banners = self

    #for banner in services_banners:
    if services_banners == services[0]:
        print(LEFTSIDE_IAM)
        return

    if services_banners == services[1]:
        print(LEFTSIDE_EC2)
        return

    if services_banners == services[2]:
        print(LEFTSIDE_S3)
        return

    if services_banners == services[3]:
        print(LEFTSIDE_LIGHTSAIL)
        return

    if services_banners == services[4]:
        print(LEFTSIDE_ROUTE53)
        return

    if services_banners == services[5]:
        print(LEFTSIDE_KMS5)
        return
