from aws.Themes.styles import *
from aws.Themes.text import *
from aws.services.ec2.ec2_menu import ec2Menu
from aws.services.kms.kms_menu import *
from aws.services.s3.s3_menu import *
from aws.services.lightsail.lightsail_menu import *
from aws.services.iam.iam_menu import *
from aws.services.route53.route53_menu import *


class Menu:

    def __init__(self):
        logoColorization()
        #self.MainMenu = display(MAIN_MENU)

    def run(self):

        main_menu = {
            "1.": iam_menu(),
            "2.": ec2Menu(),
            "3.": s3Menu(),
            "4.": lightsailMenu(),
            "5.": display(ROUTE53_MENU),
            "6.": kmsMenu(),
            "99.": exit()
        }
        while True:

            choice = choices(main_menu_text[0])
            #action = self.MainMenu.get(choice)

            if choice in main_menu:
                return choice

            else:
                print("{0} is not a valid choice ... ".format(choice))


    @staticmethod
    def exitProgram(self):
        print("THANK YOU FOR USING LEFTSIDE.VISION")
        exit(0)


if __name__ == "__main__":
    Menu().run()
