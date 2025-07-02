''' write a program to find out wheather a student has passed
or failed if it requires a total of 40% 
and at least 33% in each subject to pass. assume 3 subjects
and take marks as an input
from the user'''

marks1 = int(input("Enter marks 1 :"))
marks2 = int(input("Enter marks 2 :"))
marks3 = int(input("Enter marks 3 :"))
marks4 = int(input("Enter marks 4 :"))

# check for total percentage 
total_percentage = (( marks1 + marks2 + marks3)/300)*100

if(total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>33):
    print(" you are passed,  congratulations!", total_percentage)

else:
    print("you failed, try again next year", total_percentage)
