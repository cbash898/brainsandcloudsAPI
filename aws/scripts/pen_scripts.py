pentest = """#!/bin/bash

#get the present users
USER=`whoami`


# Get distros
ID_LIKE=`cat /etc/os-release | grep "ID_LIKE"`
ID=`cat /etc/os-release | grep "ID"`
#CENTOS=$(cat /etc/os-release | grep "rhel")
HOSTNAME=`hostname`



MenuWelcomeBoard () {

  echo '***************************   WELCOME TO HBOARD SERVER Installation Script **************************************'
  echo
  echo '[+] Starting the GCloud Installation Script ......'
  echo

}


#------------------- Function for Linux distros ----------------------------------

debian_security_settings() {

  echo "Opening ports ==>  (Defaults ports [80, 22, 443])"
  echo
  echo

  # shellcheck disable=SC1069
  # shellcheck disable=SC1020

  sudo apt-get -y update && sudo apt-get -y install ufw
  sudo systemctl enable ufw.service
  sudo systemctl start ufw.service

  ports="22 80 443 53"
  for i in $ports
  do
    sudo ufw allow $i
    if [ $? = 0 ];
    then
      echo "Complete =============>>>>>>>>>>>"
      echo
      echo

    else

      echo "Negative <<<<<<<<<<=============="
      echo
      echo

    fi
  done

}


rhel_security_settings () {




    echo "Opening ports ==>  (Defaults ports [80, 22, 443])"
    sudo yum update -y && sudo sudo yum install -y firewalld
    sudo systemctl enable firewalld

    # Services to be added permanently

    service="RH-Satellite-6 RH-Satellite-6-capsule amanda-client amanda-k5-client audit bgp bitcoin
    bitcoin-rpc bitcoin-testnet bitcoin-testnet-rpc ctdb dhcp distcc dns docker-registry docker-swarm
    finger ftp git http https imap imaps ipp ipp-client ipsec irc ircs iscsi-target isns jenkins ldap ldaps
    mysql nfs nfs3 openvpn pop3 pop3s postgresql privoxy proxy-dhcp pulseaudio puppetmaster rsh rsyncd
    samba samba-client samba-dc sane sip sips slp smtp smtp-submission smtps snmp snmptrap squid ssh svn  tftp tftp-client
    tor-socks transmission-client upnp-client vnc-server xmpp-client xmpp-local xmpp-server"

    for i in $service
    do

      sudo firewall-cmd --zone=trusted --add-service $i
      sudo firewall-cmd --zone=trusted --add-service $i --permanent

      if [ $? -eq 0 ];
      then
        echo
        echo "Command not working ...."
      else
        echo
        echo " Success ......."
      fi
    done


}


packages_installation () {

  packages="bpython netcat ncat python3-pip python-shodan python-setuptools python3-setuptools
  torsocks proxychains rkhunter bpython2 bpython3 python-setuptools etherape ettercap bzip2 ipcal
  python-virtualenv python3-virtualenv  python-aws-requests-auth python-argparse
  python3-boto python-bitbucket python-bitcoin python-bitarray python-cups python-couchdb whois
  aircrack-ng nmap python-bitcoin python-babel openvpn wget gedit acct  zsh build-essential
  sendmail proxychains fakeroot git curl openssl apache2 whowatch hydra
  nikto ldap-utils rwho sshfs  tcpdump rsh-client x11-apps finger python-elixir
  psmisc auditd aptitude bpython dnsrecon dnsenum fping arping masscan spiderfoot spiderfoot-cli
  netmask nbtscan swaks onesixtyone  netdiscover ssldump sqlmap hydra hashcat medusa john awscli"


  for i in $packages
  do
    # shellcheck disable=SC2109
    if [ $ID_LIKE == "ID_LIKE=debian" ]; then
      echo "[+] Installing packages for debian ........"
      echo

      sudo apt-get -y update && sudo DEBIAN_FRONTEND=noninteractive apt-get -y install $i
      echo
      echo

      if [ $? = 0 ];
      then
        echo "Success ================>>>>>>"
        echo
      else
        echo "Negative <<<<<==============="
        echo
      fi

    else

      echo "[+] Installing packages for RHEL DISTROS ...."
      echo
      echo
      sudo yum update -y && sudo  yum -y install $i

      if [ $? = 0 ];

      then
          echo " Success =============>>>>>>>>"
          echo

      else

          echo " NEGATIVE <<<<<<<<==========="
          echo
      fi
    fi

  done

}


github () {

  # Git clone is next
  sudo chmod 777  -R /opt/
  cd /opt/

  git clone https://github.com/hak5darren/USB-Rubber-Ducky &&
  git clone https://github.com/robertdavidgraham/masscan.git /opt/masscan &&
  git clone https://github.com/Dionach/CMSmap /opt/CMSmap &&
  git clone https://github.com/ChrisTruncer/EyeWitness.git /opt/EyeWitness &&
  git clone https://github.com/sqlmapproject/sqlmap /opt/sqlmap &&
  git clone https://github.com/cheetz/PowerSploit /opt/HP_PowerSploit &&
  git clone https://github.com/cheetz/PowerTools /opt/HP_PowerTools &&
  git clone https://github.com/cheetz/nishang /opt/nishang &&
  git clone https://github.com/secforce/sparta.git /opt/sparta &&
  git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git /opt/airgeddon &&
  git clone https://github.com/arismelachroinos/lscript.git /opt/lscript &&
  git clone https://github.com/chris408/ct-exposer.git /opt/ct-exposer &&
  git clone https://github.com/laramies/theHarvester.git &&
  git clone https://github.com/achillean/shodan-python.git


}


# -------------------------------- MAIN SCRIPT -------------------------------------------
# Get input for Name of Service Account


if [ $ID_LIKE == "ID_LIKE=debian" ];
then

  MenuWelcomeBoard

  echo '[+] Debian packages installation ......'
  echo
  echo

  # ** App **
  packages_installation
  github
  debian_security_settings

elif [ $ID == "ID=debian" ]; then

  MenuWelcomeBoard

  echo '[+] Debian packages installation ......'
  echo
  echo

  # ** App **
  packages_installation
  github
  debian_security_settings


else

  MenuWelcomeBoard

  echo 'Redhat Installation packages ......'
  echo
  echo

  packages_installation
  github
  rhel_security_settings

fi
"""
