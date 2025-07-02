''' Write a program to calculate 
the grade of student from his marks 
from the following scheme:
90 - 100 >= A
80 - 90 >= B
70 - 80 >= C
60 - 70 >= D
50 - 60 >= E
<50 >= F '''

marks = int(input("Enter you marks :"))

if(marks>90 and marks<=100):
    print(" congrats you are  Excellent")

elif(marks>80 and marks<=90):
    print(" you got grade A")

elif(marks>70 and marks<=80):
    print("you got grade B")

elif(marks>60 and marks<=70):
    print("you got grade C")
elif(marks>50 and marks<=60):
    print("you got grade D")
elif(marks<=50):
    print(" sorry, you failed")       

else:
    print("you have given invalid marks :")

print(" end..")