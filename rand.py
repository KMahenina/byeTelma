import random,time,os
from log import anim
x=11111111111111
y=99999999999999

logo=f""" \033[1;92m
        llllll  llll  ll  ll   ll    ll 
          ll    ll    ll  ll l ll  ll  ll
          ll    lll   ll  ll   ll  llllll \033[1;97m
          ll    ll    ll  ll   ll  ll  ll
          ll    llll  ll  ll   ll  ll  ll
"""
color=[
'\033[0;96m' ,
'\033[1;37m ',
'\033[1;35m' ,
'\033[1;33m' ,
'\033[1;34m' ,
'\033[1;96m' ,
'\033[1;31m'
]

print(" [+] limite >> exemple:10 ou 50 ou 100   ")
limit=int(input("\033[1;31m limit:"))

anim(logo)
print(40*'-')
for i in range(0,limit):
	c=random.choice(color)
	r=random.randint(x,y)
	time.sleep(0.5)
	print(c,"             #321*",r,"#\n")
	
print(40*'-')
print("\033[1;35 [+]Booooo 🤣")
print(40*'-')