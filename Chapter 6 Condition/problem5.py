# 5. Write a program which finds out whether a given name is present in a list or not.

l = ["saksham", "saksh", "sakshita", "sakshy", "saksh"]

name = input("Enter your name: ")

if(name in l):
    print("Name is present in the list")
else:
    print("Name is not present in the list")