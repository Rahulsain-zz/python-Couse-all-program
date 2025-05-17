#Find the largest of three numbers
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
if num1>num2 and num1>num3:
    print("largest number",num1)
elif num2>num1 and num2>num3:
    print("largest number",num2)
elif num3>num2 and num3>num1:
    print("largest number",num3)

'''other method
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
print(max(num1,num2,num3))'''
