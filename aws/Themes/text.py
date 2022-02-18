# This is a sample Python script.

# ------------------------------------------------------------------------------------------------------------------
# SERVICES
# -----------------------------------------------------------------------------------------------------------------------


MAIN_MENU = ["\n1.  IAM",
             "2.  EC2",
             "3.  S3",
             "4.  LIGHTSAIL",
             "5.  ROUTE53",
             "6.  KMS",
             "X.  Exit"]


IAM_MENU = ["\n1. IAM USERS",
            "2. IAM KEYS",
            "3. IAM POLICY",
            "4. IAM LOGIN PROFILE",
            "B. BACK TO MAIN MENU\n"
            ]


EC2_MENU = ["\n1. INSTANCE",
            "2. KEYPAIR",
            "3. SECURITY GROUPS",
            "4. NETWORK ACL",
            "5. AUTOMATE INSTANCES",
            "6. VPN AUTOMATED INSTANCES",
            "B. BACK TO MAIN MENU\n"
            ]


S3_MENU = ["\n1. BUCKET",
           "2. BUCKET WEBSITE",
           "3. CRYPTOGRAPHY",
           "B. BACK TO MAIN MENU\n"
           ]

VPN_AUTOMATED_INSTANCES = ["\n1. VPN EC2 INSTANCES",
                   "2. VPN LIGHTSAIL INSTANCES",
                   "3. RANDOM AUTOMATED VPN",
                   "B. BACK TO MAIN MENU\n"
           ]


LIGHTSAIL_MENU = ["\n1. Get Servers",
                  "2. Create Servers",
                  "3. Start Servers",
                  "4. Stop Servers",
                  "5. Delete Servers",
                  "6. Get Opened Ports",
                  "7. Open New Ports",
                  "8. Allocate StaticIp"
                  "9. Attach StaticIp",
                  "10. Detach StaticIp",
                  "11. Get SnapShots",
                  "12. Delete SnapShots",
                  "13. Export SnapShots",
                  "14. Automate Server",
                  "B. Back to Menu \n"]


ROUTE53_MENU = ["\n1. DNS MANAGEMENT",
                "2. TRAFFIC MANAGEMENT",
                "3. DOMAIN POLICY",
                "4. REGISTER DOMAIN",
                "5. AUTOMATE ALL",
                "B. BACK TO MAIN MENU\n"
                ]

# ----------------------------------------------------------------------------------------------------


SUB_IAM_MENU = ["\n1. Create users",
                "2. Get users",
                "3. Update users",
                "4. delete users",
                "B. Back to iam Menu\n"
                ]


SUB_IAM_KEYPAIRS_MENU = ["\n1. Get Keypairs",
                         "2. Create Keypairs",
                         "3. delete Keypairs",
                         "B. Back to iam Menu\n"
                         ]

SUB_KMS_MENU = ["\n1.  Create Customer Master Key",
                    "2.  List Customer Master Keys",
                    "3.  Generate Data Key",
                    "4.  Decrypt Data Key",
                    "5.  Change Region",
                    "6.  Schedule Keys Deletion",
                    "7.  Enable Customer Master Keys",
                    "8.  Disable Customer Master Keys",
                    "9.  Encrypt File",
                    "10.  Decrypt File",
                    "B.  Back to iam Menu\n"
                ]



SUB_IAM_POLICY_MENU = ["\n1. Get Policy",
                       "2. Attach policy",
                       "3. Detach policy",
                       "B. Back iam Menu\n"
                      ]


SUB_IAM_LOGINPROFILE_MENU = ["\n1. Create LoginProfile",
                             "2. Check LoginProfile",
                             "2. Delete LoginProfile",
                             "4. Reset LoginProfile",
                             "B. Back iam Menu\n"
                      ]


SUB_EC2_MENU = ["\n1. Create Instances",
                "2. Get Instances",
                "3. Start Instances",
                "4. Stop Instances",
                "5. Delete Instances",
                "6. Schedule Instances",
                "B. Back ec2 Menu\n"
                ]


SUB_EC2_KEYPAIR_MENU = ["\n1. Get Keypairs",
                        "2. Create Keypair",
                        "3. Delete Keypairs",
                        "B. Back to ec2 Menu"]



SUB_EC2_SECURITYGROUP_MENU = ["\n1. Get SecurityGroups",
                              "2. Create SecurityGroup",
                              "3. Delete SecurityGroup",
                              "B. Back ec2 Menu\n"]


SUB_EC2_NETWORKACL_MENU = ["\n1. Create Entries"
                           "2. Create Tags",
                           "3. Delete",
                           "4. Delete Entry",
                           "5. Load",
                           "6. Replace Associations",
                           "B. Back to Network Menu\n"]



SUB_S3_MENU = ["\n1. Get Buckets",
               "2. Create Buckets",
               "3. upload Files",
               "4. Downloads Files",
               "5. Encrypt and Decrypt",
               "6. Delete Object",
               "7. Get ACL",
               "8. Delete Bucket",
               "B. Back to S3 Menu\n"
               ]


SUB_S3_CRYPTO_MENU = ["\n1. Get Bucket Encryption",
                      "2.  Encrypt Bucket",
                      "3.  Decrypt Bucket",
                      "4.  Delete Bucket Encryption",
                      "B.  Back to S3 Menu\n"
                      ]


SUB_ROUTE53_MENU = ["\n1. Create Domain",
                    "2. Create Health Check",
                    "3. Delete Health Check",
                    "4. Get IP Check Ranges",
                    "5. Get Traffic Policy",
                    "6. Create Traffic Policy",
                    "7. Delete Traffic Policy ",
                    "8. Get GeoLocation",
                    "9. List Hosted Zones",
                    "B. Back to ROUTE53 Menu\n"
                    ]


vpnLocations = ['\n1. ap-east-1',
                '2. ap-south-1',
                '3. ap-northeast-3',
                '4. ap-northeast-2',
                '5. ap-southeast-1',
                '6. eu-south-1',
                '7. eu-south-1',
                '8. af-south-1'
              ]

# -----------------------------------------------------------------------------------------------------------------------
# TEXT
# -----------------------------------------------------------------------------------------------------------------------

Session_Text = ["Enter the aws_access_key_id= ",
                "Enter the aws_secret_access_key= ",
                "region_name= "
                ]

main_menu_text = ["\nEnter Menu Choice:  "]

main_menu_exit = ["Enter 99 to exit Menu: "]


iam_text_user = ["Enter UserName: ",
                 "Enter NewUserName: ",
                 "Enter NewPassword: ", ]

iam_text_key = ["Enter KeyName: "]

iam_text_policy = ["Enter Policy Name", "Enter Scope (ALL | LOCAL | AWS ): "]

ec2_text_instance = ["Enter keyName: ",
                     "Enter GroupName: ",
                     "Enter CIDR: ",
                     "Enter SecurityGroup Description (Not more that 50 Letters): ",
                     "Enter the IpProtocol {tcp/udp}: ",
                     "Enter Path to Local UserData: ",
                     "Enter InstanceType(t2.micro|t2.small|t2.medium|t3.nano|t3.micro|t3.small|t3.medium): ",
                     "Enter AvailabilityZone(us-west-2a|us-west-2b|us-east-2a|us-east-1b): ",
                     "Enter VolumeSize (int): ",
                     "Enter VolumeType (standard | io1 | gp2): "]


ec2_text_keys = ["Enter KeyName: ",
                 "Enter KeyDir: ",
                 "Enter SecurityGroupName: ",
                 "Enter SecurityGroup Descriptions(50 Letters): "]



vpnLocationsOptions = ['Enter the Geographical Zone: ']


lightsail_text = ["Enter serverName: ",
                 "Enter KeyName: ",
                 "Enter AvailabilityZone: ",
                 "Enter ServerIP: ",
                 "Enter Ports: "]


KMS_CustomerMasterKeySpec = ['RSA_2048',
                            'RSA_3072',
                            'RSA_4096',
                            'ECC_NIST_P256',
                            'ECC_NIST_P384',
                            'ECC_NIST_P521',
                            'ECC_SECG_P256K1',
                            'SYMMETRIC_DEFAULT']


KMS_ALGORITHM = ['SYMMETRIC_DEFAULT', 'RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256']


KMS_TEXTS = ["Enter CMK Name: ",
             "Enter Desc: ",
             "Enter CMK ID: ",
             "Enter CMK SPEC (RSA_3072 | RSA_4096 | ECC_NIST_P521 | ECC_SECG_P256K1 ): ",
             "Enter Limit: ",
             "Enter REGION: ",
             "Enter FILENAME: ",
             "Enter Schedule Days (int): "
             ]


KMS_Origin = ['AWS_KMS',
              'EXTERNAL',
              'AWS_CLOUDHSM']


KMS_CRYPTOGRAPHY = ["Enter Encryption FILENAME: "
                    ]


s3_text_words = ["Enter the BucketName: ",
                 "Enter REGION (us-west-2): ",
                 "Enter FILENAME (/tmp/hello.txt): ",
                 "Enter OBJECTNAME (hello.txt): "]

text_error = ["\n!!! Please select from the right option !!!\n"]

menu_agreement = ("""

The responsibilities of a program office are varied. These include:

Clearly communicating the open source strategy within and outside the company
Owning and overseeing the execution of the strategy
Facilitating the effective use of open source in commercial products and services
Ensuring high-quality and frequent releases of code to open source communities
Engaging with developer communities and seeing that the company contributes back to other projects effectively
Fostering an open source culture within an organization
Maintaining open source license compliance reviews and oversight

""")


