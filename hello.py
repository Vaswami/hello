'''name = input("what is your name ? ")
color =input("what is your favirot color ")
print(name + " likes " + color)


birth_year =input("birth year :")
print(type (birth_year ))
age =2019 - int(birth_year)
print( type  (age) )
print(age)



first = "jenifier"
last = " vastrada"
#meaasge= first + ' [ ' + last + ' ] is a coder
msg = f'{first} [{last}] is a coder'
print (msg)


import math
x = 3
print(abs(-x))
print(round(x) )
print(math.factorial(x))


name ='swami'
if len(name)<3:
    print ("name is less than 3")
elif len(name)>5:
    print("name is greater than 5")
else:
    print('namd looks good')


# conveter proram
weight =int(input('weight : '))
choice=input('l(bs) or k(kg) : ')
if choice=='k':
    kgs=weight*0.45
    print(f'weight in  {kgs}  kgs')
elif choice=='l':
    lbs=weight/0.45
    print(f"weight in {lbs}  pound ")
else:
    print("invalied choice")

# Gussing program
screct =20
count=0
while count<3:
    num=int(input("Guesss : ") )
    count = count + 1
    if num ==screct :
        print("you won !" )
        break
else:
    print("you loss")


#car game
user=""
stared = False
while True:
    user =input(">")
    if user =="start":
        if stared :
            print(" car is already started ")
        else:
            stared=True
            print("start the car ")
    elif user == "stop":
        if not stared:
            print("car is already stoped  ")
        else:
            stared=False
            print("car is stoped")
    elif user == "help":
        print(
    start -- to start the car
    stop  -- to stop the car
    qiut -- to ext)
    elif user =="quit":
        break
    else:
        print("I didnt understand what u enterd")


user = ""
stared = "stop"
while True:
    user = input(">")
    if user == "start":
        if stared == "start":
            print(" car is already started ")
        else:
            stared = "start"
            print("start the car ")
    elif user == "stop":
        if stared != "start":
            print("car is already stoped  ")
        else:
            stared = "stop"
            print("car is stoped")
    elif user == "help":
        print(
        start -- to start the car
        stop  -- to stop the car
        qiut -- to ext)
    elif user == "quit":
        break
    else:
        print("I didnt understand what u enterd")



# Gussing program
screct =20
count=0
while count<3:
    num=int(input("Guesss : ") )
    count = count + 1
    if num ==screct :
        print("you won !" )
        break
else:
    print("you loss")

phone =input('phone: ' )
digits={
    "1":"for ",
    "2":"Two",
    "3":"Three"
}
output= ""
for i in phone:
    output += digits.get(i,"!") + " "
print(output)'''

'''from array import *
arr =array ('u',[])
n = int(input("enter the size of an array" ))
for i in range(n):
    m = input( "ente the next element " )
    arr.append(m)
print(arr)

ele =input("enter the serched element " )
k=0
for e in arr:
    if e==ele:
        print(k)
        break
    k=+1'''

from myfirst import *
def fun1():
    add()
    print(" print  one and \v  \f Fun1")
def fun2():
    print("Print \r Fun2")

def main():
    fun1()
    fun2()

main()