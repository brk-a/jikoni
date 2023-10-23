#!/usr/bin/env python3

'''
create and validate a "secure password"
1. at least 8 chars
2. at least 2 special chars
3. both capital and small letters
4. at least 1 digit
'''

from string import ascii_letters, digits
from random import choices
from sys import argv, exit
import re

def secure_password():
    if len(argv)!=2:
        print("Usage: ./0-secure_pass <your_password_length>")
        exit(1)

    # inp = int(input("Enter password length... "))
    inp = argv[1]
    # c = ascii_letters+digits+'#$%&*+-@?:!£'
    c = f'{ascii_letters}{digits}#$%&*+-@?:!£'
    passwds = [''.join(choices(c, k=inp)) for i in range(50)]
    rgx = ['\W', '[a-z]', '[A-Z]', '\d']

    for i in passwds:
        x = len([*filter(lambda x: re.search(x, i), rgx)])
        if x==4:
            print(f'Your secure password: {i}')
            break

# if len(x)>=7 and len(re.findall(r'\W{2,}', )) and len(re.findall(r'\d{2,}', x)):
#     print("Password not valid")
# else:
#     print("Password is valid")

if __name__=="__main__":
    secure_password()
