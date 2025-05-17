#Factorial of a number
sum=1
num=int(input("enter factorial number"))
for i in range(1,num+1):
    sum*=i
print("factorial:- ",sum)
