# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

# in statement

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

text = input("Enter your comment: ")

if(p1 in text):
    print("This comment is spam")
elif(p2 in text):
    print("This comment is spam")
elif(p3 in text):
    print("This comment is spam")
elif(p4 in text):
    print("This comment is spam")
else:
    print("This comment is not spam")