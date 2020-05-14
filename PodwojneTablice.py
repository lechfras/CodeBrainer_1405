a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])

print(a[0][2])
b= a[0]
print(b)
b[2]=9
print(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print