#Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
      return "a is greatest"
    elif(b>a and b>c):
       return "b is greatest"
    else:
       return "c is greatest"
   
a = 55
b = 45
c = 30

print(greatest(a,b,c))
    