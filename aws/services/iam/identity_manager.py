import logging
import yaml
from botocore.exceptions import ClientError
from aws.envsetup.config import client, resource


logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


class IAM_USER:

    def __init__(self):
        # self.username = input("Enter the username")
        # self.connect = AWSConnect.client("iam")
        pass

    def create_iam_user(self):

        # connect = boto3.client("iam")
        user = client("iam").create_user(UserName=self)
        print(yaml.dump(user))

    def getUsers(self=2):

        user = client("iam").list_users(MaxItems=self)

        import yaml
        print(yaml.dump(user['Users']))

    def update_iam_user(self, newUser):

        user = client("iam").update_user(UserName=self, NewUserName=newUser)
        print(yaml.dump(user))

    def delete_iam_user(self):

        try:
            user = client("iam").delete_user(UserName=self)
            print(yaml.dump(user))

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True


class IAM_KEYS:

    def __init__(self):
        pass


    def getKeys(self, maxItems=None):

        try:
            user = client("iam").list_access_keys(UserName=self, MaxItems=int(maxItems))
            for ids in user['AccessKeyMetadata']:
                print("\nUserName: {}".format(ids['UserName']),
                     "\nAccessID:  {}".format(ids['AccessKeyId']),
                    "\nStatus: {}".format(ids['Status']),
                    "\nCreateDate: {}".format(ids['CreateDate'])
                   )

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True


    def create_key(self):

        Filename = "/tmp/" + self + ".txt"
        try:
            user = client("iam").create_access_key(UserName=self)

            with open(Filename, "w") as kg:
                print(user['AccessKey'], file=kg)

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True


    def delete_key(self, accessKeyId):

        try:
            user = client("iam").delete_access_key(UserName=self, AccessKeyId=accessKeyId)
            print(yaml.dump(user))

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True


#--------------------------------------------------------------------------------------------------

class IAM_POLICY:

    def __init__(self):
        pass

    # CBTC
    def createPolicy(self, polDoc):

        # Create a policy
        my_managed_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "logs:CreateLogGroup",
                    "Resource": "RESOURCE_ARN"
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "dynamodb:DeleteItem",
                        "dynamodb:GetItem",
                        "dynamodb:PutItem",
                        "dynamodb:Scan",
                        "dynamodb:UpdateItem"
                    ],
                    "Resource": "RESOURCE_ARN"
                }
            ]
        }

        create_policy = client("iam").create_policy(
            PolicyName=self,
            PolicyDocument=polDoc
        )
        for pol in create_policy['Policies']:
            print(yaml.dump(pol))


    def getPolicy(self, maxItems):

        getPols = client("iam").list_policies(Scope=self, MaxItems=int(maxItems))
        for pols in getPols['Policies']:
            print(yaml.dump(pols))

    def attach_policy(self, arn):
        attach_policy = client("iam").attach_role_policy(PolicyArn=arn,
    RoleName=self)
        for pols in attach_policy['Policies']:
            print(yaml.dump(pols))


    def detach_policy(self, arn):

        attach_policy = client("iam").detach_role_policy(PolicyArn=arn,
                                                         RoleName=self)
        for pols in attach_policy['Policies']:
            print(yaml.dump(pols))


class LoginUser:

    def __init__(self):
        pass


    def create_login(self, password):

        try:

            login = resource("iam").loginProfile(self)
            create_password = login.create(Password=password, PasswordResetRequired=False)
            print(create_password)

        except:

            logger.warning("Wrong Option")
            return False
        return True


    def checkLoginProfile(self):

        pass


    def deleteLoginProfile(self):

        pass


    def resetLoginProfile(self):

        pass


    def create_loginProfile(self, password):

        Filename = "/tmp/" + self + "_loginProfileDoc.txt"
        try:
            user = resource("iam").LoginProfile(self)
            login_profile = user.create(Password=password, PasswordResetRequired=True)

            with open(Filename, "w") as kg:
                print(login_profile, file=kg)

        except ClientError as e:
            if e.response['Error']['Code'] == "EntityAlreadyExists":
                logger.error("Entity Exists")
                return False
            return True




