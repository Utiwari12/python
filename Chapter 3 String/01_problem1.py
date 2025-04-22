# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(f"Hello, {name}! You are {age} years old.")

letter = ''' Dear <|Name|>,
             You are selected on
             <|Date|>'''
             
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "15 June"))

name = "Harry is a good boy and he is . . not a bad boy"

print(name.find("Harry"))
print(name.find("boy"))
print(name.find(""))
print(name.find("bad"))