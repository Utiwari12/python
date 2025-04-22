#1. Write a program to read the text from a given file ‘poems.txt’ and find out 
#whether it contains the word ‘twinkle

f = open('poem.txt', 'r')
content = f.read()
if('twinkle' in content):
    print("Yes, it contains twinkle")
else:
    print("No, it doesn't contain twinkle") 

f.close()