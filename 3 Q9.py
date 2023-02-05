a=[]
n=int(input("Enter M for M x N matrix: "))
print("Enter the element: ")
for i in range(n):
    row=[]
for j in range(n):
    row.append(int(input()))
a.append(row)
print(a)
print("Display array in matrix form")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
b=[]
m=int(input("Enter N for M x N matrix: "))
print("Enter the element: ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    b.append(row)
print(b)
print("Display array in matrix form: ")
for i in range(n):
    for j in range(n):
        print(b[i][j], end=" ")
    print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]
    print("Resultant matrix is: ")
for r in result:
    print("Resultant matrix is: ")
