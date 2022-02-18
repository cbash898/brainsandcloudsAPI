import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


#s3ErrorHandler.testBucketExists("Hududuedne")

IAM = [
    "iam.Client.exceptions.InvalidInputException",
    "iam.Client.exceptions.NoSuchEntityException",
    "iam.Client.exceptions.LimitExceededException",
    "iam.Client.exceptions.ServiceFailureException"
]


EC2 = [
    "",
    "",
    "",
    "",
    ""
]


S3 = [
    "S3.Client.exceptions.BucketAlreadyExists",
    "S3.Client.exceptions.BucketAlreadyOwnedByYou"
]


Lightsail = [
    "Lightsail.Client.exceptions.ServiceException",
    "Lightsail.Client.exceptions.InvalidInputException",
    "Lightsail.Client.exceptions.NotFoundException",
    "Lightsail.Client.exceptions.OperationFailureException",
    "Lightsail.Client.exceptions.AccessDeniedException",
    "Lightsail.Client.exceptions.AccountSetupInProgressException",
    "Lightsail.Client.exceptions.UnauthenticatedException"
]


Route53 = ["Route53.Client.exceptions.ConcurrentModification",
           "Route53.Client.exceptions.NoSuchKeySigningKey",
           "Route53.Client.exceptions.InvalidKeySigningKeyStatus",
           "Route53.Client.exceptions.InvalidSigningStatus",
           "Route53.Client.exceptions.InvalidKMSArn"
]


