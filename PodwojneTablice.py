"""
a = [[1, 2, 3], [4, 5, 6]]

print(a[0])
print(a[1])

print(a[0][2])
b= a[0]
print(b)
b[2]=9
print(b)

print(len(a))

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')


s =0
for i in range(len(a)):
    for j in range(len(a[i])):
        s+=a[i][j]
print(s)

###Zadanie
# mamy tablice n x m wypelnic "." "*"
"""
n,m =[int(i) for i in input().split()]
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        if (i+j)%2==0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))