a = int(input("Enter your age: "))

#if elif else ladder

if(a >= 18):
    print("You can vote")
    print("Thank you")
    
elif(a<0):
    print("Invalid negativ age")
    
elif(a==0):
    print("You are entering 0 which is not a valid age")
    
else:
    print("You cannot vote")
    print("Thank you")
    
print("End of program")