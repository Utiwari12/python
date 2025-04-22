#Write a program to calculate the factorial of a given number using for loop.
#5! = 5*4*3*2*1 = 120

n = int(input("Enter the number: "))

fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)