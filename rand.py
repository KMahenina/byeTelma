import random,time,os
x=11111111111111
y=99999999999999
color=[
'\033[0;96m' ,
'\033[1;37m ',
'\033[1;92m' ,
'\033[1;35m' ,
'\033[1;33m' ,
'\033[1;34m' ,
'\033[1;96m' ,
'\033[1;31m'
]


limit=int(input("\033[1;37m limit:"))
print("      ")
for i in range(0,limit):
	c=random.choice(color)
	r=random.randint(x,y)
	time.sleep(0.5)
	print(c,"#321*",r,"#")
