# number =[5,2,5,2,2]
'''for i in range (5):
    for j in range (4-i):
        print(j+1,end= '')
    print()


num =[2,3,5,8,89,8,3,4,110]
num.sort()
num.reverse()
print(num)
max =num[0]
for i in num:
    if i>max:
        max=i
print(max)'''

'''print("enter the starting number")
upper =int(input())
print("enter the ending number")
lower =int(input() )
for num in range(lower,upper+1):
    if num >1:
        for i in range (2,num):
            if num%i==0:
                break
    else:
        print(num)'''

def add():
    print("add the result",__name__)
def sub():
    print("substract the result")

def main():
    add()
    sub()
if __name__ =="__main":
    main()
