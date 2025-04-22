a = (1,2, 5, 6, 324, 3424, "Apple", "Banana", "Cherry" , 5 , 345.07, False, "Aakash", "Rohan")

print(a, type(a))

b = (2)
print(b, type(b))

no = a.count("Apple")
print(no)

no = a.index("Apple")
print(no)

no = a.index("Cherry")
print(no)

no = a.__add__((1,2, 5, 6, 324, 3424, "Apple", "Banana", "Cherry" , 5 , 345.07, False, "Aakash", "Rohan"))
print(no)

no = a.__len__()
print(no)