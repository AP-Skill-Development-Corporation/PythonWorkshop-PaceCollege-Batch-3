from getpass import getpass 
uname=input('enter u name:-')
pwd=getpass('enter pwd :-')

if uname=="sai"and pwd=="sai@123":
    print('Welcome',uname)
else:
    print('Invalid uname or password')
