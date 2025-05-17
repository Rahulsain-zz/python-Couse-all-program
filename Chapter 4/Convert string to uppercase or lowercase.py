#Convert string to uppercase/lowercase
print("select '1' for Convert string to uppercase")
print("select '2' for Convert string to lowercase")
select=int(input("select 1/2 :- "))
if select==1:
    name=input("enter string:- ")       
    print(name.upper())
elif select==2:
    name=input("enter string:- ")       
    print(name.lower())
