''' Write a program to find out 
wheather a given post  is talking about "harry" or not'''

post = (input("Enter your post : "))

if("Harry".lower() in post.lower()):
    print("this post is talking about harry")

else:
    print("this post is not talking about harry")    
print("end...")

