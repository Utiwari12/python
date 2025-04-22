a = int(input("Enter your age: "))

#if statement no: 1
if(a%2==0):
    print(" a is Even number")
else:
    print("a is odd number")
 
 # End of if statement no: 1   

#if statement no: 2

if(a >= 18):
    print("You can vote")
    print("Thank you")
    
elif(a<0):
    print("Invalid negativ age")
    
    
else:
    print("You cannot vote")
    print("Thank you")
    
# End of if statement no: 2
    
print("End of program")