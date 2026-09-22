
#sign in 
import json

    
name=input("Enter Name: ")
password=input("Enter Password: ")

with open("users.json","r") as file:
    users=json.load(file)

if name ==users["name"] and password == users["password"]:
 print("-------Sign In Successfull-------") 
else:
    print("Invalid Email and Password")


