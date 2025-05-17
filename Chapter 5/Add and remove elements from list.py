#Add and remove elements from list
a=[]
print("use add")
print("use remove")
print("use show")
print("use exit") 
while True:
    n=input("enter you add/remove/show:-  " )
    if n=="add":
        name=input("type...  ")
        a.append(name)
    elif n=="remove":
        name=input("type...  ")
        a.remove(name)
    elif n=="show":
         print(a)
    elif n=="exit":
        break
