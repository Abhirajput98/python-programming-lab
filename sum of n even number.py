a=int(input("entr the value of n"))
sum=0

for i in range(1,a+1):
    if(i/2==0):
        sum=sum+i
        i=i+1

print(sum)