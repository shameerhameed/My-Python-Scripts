###########################################################################
# domain check.py                                                         #
# The script will check if a particualar fqdn exists.                     #
# Written by Shameer Hameed                                               #
# Version 1.0    21-April-2018                                            #
#
# Usage: ./domaincheck.py -c hostname -d domainname1,domain2,... domain n
# eg: ./domaincheck.py -c example -d com net org biz                                     #
###########################################################################



import argparse
import socket
def check_fqdn(hName,dName):
    for dn in dName:
       fqdn = hName + "." + dn
       try:
         if socket.gethostbyname(fqdn):
           print("Found {}" .format(fqdn))
       except socket.gaierror:
           print("Not Found {}" .format(fqdn))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='domain name check')
    parser.add_argument('-c', '--client',help = "Adding client")
    parser.add_argument('-d','--domain', help = "Adding domains",nargs='+')
    arg = parser.parse_args()
    try:
       if( arg.client or arg.domain):
          check_fqdn(arg.client,arg.domain)
    except:
        print("Please provide both -c and -d")


