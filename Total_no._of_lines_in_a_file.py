f=open('a.txt','r')
sum=0
str=f.read()
print(str)
for i in str:
    if i=='\n':
        sum+=1
print(sum)
f.close()
