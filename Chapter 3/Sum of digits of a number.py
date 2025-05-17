#Sum of digits of a number
sum=0
num=input("enter number")
for i in range(len(num)):
    a=int(num[i])
    sum+=a
print(sum)
