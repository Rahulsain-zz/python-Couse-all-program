#Grade calculation system (A, B, C based on marks)
'''Grade	Scale	Grade Description	US Grade
70.00 - 100.00	First Class with Distinction/
                First Division with Distinction	A+
60.00 - 69.99	First Class/First Division	A
50.00 - 59.99	Second Class/Second Division	B
40.00 - 49.99	Third Class/Third Division/Pass Class	C
G 36.00-39.99	Conceded Pass/Grace Marks	D
P		Pass	S
F	0.00 - 35.99	Below Minimum Pass	F'''
num=float(input("enter total number"))
if num>=70:
    print("First Division with Distinction 'A+'")
elif(num>=60):
    print("First Class/First Division 'A'")
elif(num>=50):
    print("B")
elif(num>=40):
    print("C")
elif(num>=36):
    print("D")
elif(num<36):
    print("FAIL 'F'")

