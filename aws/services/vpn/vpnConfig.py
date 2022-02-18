

# ------------------------------ NETWORKING CONNECTION --------------------------

CIDR_BLOCK = ['10.0.0.0/24']


IP_PERMISSION = [{
    'IpProtocol': 'TCP',
    'FromPort': 10035,
    'ToPort': 10035,
    'IpRanges': [{'CidrIp': CIDR_BLOCK}]
}, {
    'IpProtocol': 'TCP',
    'FromPort': 16000,
    'ToPort': 17000,
    'IpRanges': [{'CidrIp': CIDR_BLOCK}]
}, {
    'IpProtocol': 'TCP',
    'FromPort': 22,
    'ToPort': 22,
    'IpRanges': [{'CidrIp': CIDR_BLOCK}]
}]

# -------------------------------  IMAGES OF AWS-OS ----------------------------

""" IMAGES OF aws """

ImageIdUbuntu = ["ami-0ca5c3bd5a268e7db",
                 "ami-0047c52ed2f1519a3",
                 "ami-007d3f6486d9d3e6c",
                 "ami-008dcc948fb88a63a"
                 ]


ImageIdDebian = ["ami-97b790ef",
                 "ami-b4f8edcd",
                 "ami-cbad0eb3",
                 "ami-818eb7b1"
                 ]


ImageIdCentos = ["ami-00a092bd80d7ff7dd",
                 "ami-00b6409ca5f35471f",
                 "ami-00d11f107a772bf8d",
                 "ami-010afb7ef35a5c1ea"
                 ]


ImageIdAmazon = ["ami-036c394a8b6e11a45",
                 "ami-03920bf5f903e90d4",
                 "ami-041fcb43d4730cf32",
                 "ami-05a8e8d7f6573b136",
                 ]



# ------------------------  INSTANCE TYPE -------------------------------------

InstanceType = ["t1.micro",
                "t2.nano",
                "t2.micro",
                "t2.small",
                "t2.medium",
                "t2.large"
                ]

# ------------------------ REGION ZONES --------------------------------------

VpnRegions = ['ap-east-1',
                'ap-south-1',
                'ap-northeast-3',
                'ap-northeast-2',
                'ap-southeast-1',
                'eu-south-1',
                'eu-south-1',
                'af-south-1'
              ]

# --------------------  -----------------------------------------------------

BOOLEAN = True
