#Find largest and smallest in a list
a=[]
n=int(input("enter how maney number put in list:- "))
for i in range(n):
    d=int(input("enter number:- "))
    a.append(d)
print("list:- ",a)
print("largest number:- ",max(a))
print("smallest number:- ",min(a))
