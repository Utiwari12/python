f = open("file.txt", "r")

print(f.read())

f.close()

# The above code can be written as
with open("file.txt", "r") as f:
    print(f.read())
    
# you dont have to close the file