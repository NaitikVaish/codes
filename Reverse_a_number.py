num=int(input("enter the number:"))
rev=0
while(num>0):
    rem=num%10
    rev=10*rev+rem
    num=num//10
print(rev)
