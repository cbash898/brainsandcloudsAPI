from aws.Themes.styles import *
from aws.Themes.text import *
from aws.services.ec2.ec2_menu import *
from aws.services.kms.kms_menu import *
from aws.services.s3.s3_menu import *
from aws.services.lightsail.lightsail_menu import *
from aws.services.iam.iam_menu import *
from aws.services.route53.route53_menu import *
from aws.envsetup.config import *
from colorama import Fore


class AWSSessions:

	def __init__(self):
		pass





def AgreementsCheckFile():

	try:
		if not os.path.exists("agreement.txt"):
			with open("agreement.txt", "wt") as agree_file:
				agree_file.write("; YES TO AGREEMENT")
				agree_file.close()

		else:
			#print("[+] Agreement File created Already....")
			pass

	except IOError as e:
		logger.error(e)
		return False
	return True




def Agreements():

	print(Fore.RED + menu_agreement)

	agreementPolicies = input("Enter (Y|y|N|n): ")
	if agreementPolicies == "Y" or agreementPolicies == "y":
		AgreementsCheckFile()
		sleep(3)


	elif agreementPolicies == "N" or agreementPolicies == "n":
		print(Fore.WHITE + "THANK YOU FOR USING LEFTSIDE.VISION")
		exit(0)

	else:
		print("Enter the write OPTIONS PLEASE .....")
		Agreements()

	return True


def sessionFileProbe():

	aws_id = input("Enter ID: ")
	aws_secret = input("Enter Secret: ")
	regional = input("Enter Zone: ")

	try:
		if os.path.exists("aws_configure_file.ini"):
			print("[+] Config File created Already....")
			pass
		else:
			with open("aws_configure_file.ini", "wt") as session_file:
				session_file.write("; config.ini\n ; AWS Configuration file\n\n [default] \n aws_access_key_id = %s \n aws_secret_access_key = %s \n regional_zone = %s" % (aws_id, aws_secret, regional))
				session_file.close()
	except IOError as e:
		logger.error(e)
		return False
	return True



def main_menu():

	CC = "0"
	while CC == "0":

		# Improved version
		display(MAIN_MENU)

		print("\n")
		CC = input(main_menu_text[0])

		if CC == "1":
			iam_menu()

		elif CC == "2":
			ec2Menu()

		elif CC == "3":
			s3Menu()

		elif CC == "4":
			lightsailMenu()

		elif CC == "5":
			display(ROUTE53_MENU)

		elif CC == "6":
			kmsMenu()

		elif CC == "X" or CC == "x":

			print(Fore.YELLOW + "THANK YOU FOR USING LEFTSIDE.VISION")
			exit(0)

		else:
			print(text_error[0])
			main_menu()

		return CC


def main():

	shell("clear")
	logoColorization()

	if os.path.exists("agreement.txt"):
		main_menu()

	elif not os.path.exists("agreement.txt"):
		Agreements()
		sessionFileProbe()
		main_menu()

	else:
		exit(0)


if __name__ == "__main__":
	# Running the Main
	main()
