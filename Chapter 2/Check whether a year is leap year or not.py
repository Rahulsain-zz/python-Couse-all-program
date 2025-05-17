#Check whether a year is leap year or not
num=int(input("please enter year"))
if num%4==0 and (num%400==0 or num%100!=0):
    print("leap year")
else:
    print("not leap year")
