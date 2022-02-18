#!/usr/bin/env bash


USER=`whoami`
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
BOTO_CONFIG=""
CREDENTIALS="/home/$USER/.aws"
FILE="/home/$USER/.aws"



installation_package() {

  pip3 install --upgrade awscli boto3
  echo ""
  echo ""


}


aws_configure()  {

  echo ""
  echo ""

  if [ $? -eq "0"];

  then

    echo "Something went wrong ..... "

  else

    touch $FILE <<EOF





EOF



}








