#Check if string is a palindrome
name=input("enter string:- ")
if (name==name[::-1]):
   print("yes,string is a palindrome")
else:
    print("No,string is a palindrome")
