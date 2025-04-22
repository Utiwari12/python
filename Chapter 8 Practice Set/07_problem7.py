'''
Write a python function to remove a given word from a list ad strip it at the same
time

'''
def remove_word(l, word):
    n = []
    
    for item in l:
        # l.remove(word)
        # return l
        if item != word:
            n.append(item.strip(word))
    return n
l = ["hello", "world", "python", "is", "great", "think"]

print(remove_word(l, "is"))
print(remove_word(l, "python"))