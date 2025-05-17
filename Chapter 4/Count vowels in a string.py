#Count vowels in a string
count=0
word=input("enter your word")
for i in range(len(word)):
    if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
        count+=1
print("vowel",count)
