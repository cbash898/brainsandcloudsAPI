from aws.services.iam.iam_menu import *
from aws.services.s3.s3_menu import *
from aws.services.lightsail.lightsail import *
from aws.services.kms.kms_menu import *
from aws.services.ec2.ec2_menu import *
from aws.Themes.text import *
from aws.Themes.images import *
from aws.Themes.styles import *
from aws.envsetup.config import *
from time import sleep


def lightsailMenu():

    shell("clear")
    banners("lightsail")
    display(LIGHTSAIL_MENU)
    CC = input(main_menu_text[0])

    # Picking the options
    if CC == "1":
        LightSail.getServers()
        sleep(5)
        lightsailMenu()

    elif CC == "2":
        LightSail.createServer(choices(lightsail_text[0]),
                               choices(lightsail_text[1]))
        sleep(5)
        lightsailMenu()

    elif CC == "3":
        LightSail.startServer(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()

    elif CC == "4":
        LightSail.stopServer(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()

    elif CC == "5":
        LightSail.deleteServer(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()

    elif CC == "6":
        LightSail.getServers()
        LightSail.getPorts(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()

    elif CC == "7":
        LightSail.getServers()
        LightSail.openPorts(choices(lightsail_text[0]),
                            choices(lightsail_text[3]),
                            choices(int(lightsail_text[4]))
                            )
        sleep(5)
        lightsailMenu()
        
    elif CC == "8":
        LightSail.getServers()
        LightSail.grabbing_staticIp(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()
        
    elif CC == "9":
        LightSail.getServers()
        LightSail.connect_staticIp(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()
        
    elif CC == "10":
        LightSail.getServers()
        LightSail.disconnect_staticIp(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()
        
    elif CC == "11":
        LightSail.getServers()
        LightSail.grab_snapshots(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()
        
    elif CC == "12":
        LightSail.getServers()
        LightSail.remove_snapshots(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()
        
    elif CC == "13":
        LightSail.getServers()
        LightSail.exports_snapshots(choices(lightsail_text[0]))
        sleep(5)
        lightsailMenu()

    elif CC == "14":
        LIGHTSAIL_AUTOMATION.automatedServer("tedserve23980", "tedkey292")
        sleep(3)
        lightsailMenu()

    elif CC == "B" or "b":
        main.main_menu()

    else:
        print(text_error)
        lightsailMenu()

    return CC
