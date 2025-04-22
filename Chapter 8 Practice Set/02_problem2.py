# Write a python program using function to convert Celsius to Fahrenheit.
# Formula: F = (C * 9/5) + 32
# C = (F - 32) * 5/9

def f_to_c(f):
    return (f - 32) * 5/9
f = int(input("Enter the temperature in Fahrenheit: "))
c = f_to_c(f) 
print(f"{round(c, 2)}°C")
