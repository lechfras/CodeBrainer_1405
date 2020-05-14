a=set([1, 2, 3, 4, 5, 6])
b=set([4, 5, 6, 7, 8, 9])

print(a)
print(b)

#Set union
print("Set Union")
k=a|b
print(k)

#Set Intersection
print("Set Intersection")
k=a&b
print(k)

# SetDifferences
print("Set Differences")
k=(a-b)
print(k)

#Set Symmetric Differences
print("Set Symmetric Differences")
k=(a^b)
print(k)
