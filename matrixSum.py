#Taking matrix input

def matrix(m,n):
    O = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input("Enter value Matrix "))
            row.append(inp)
        O.append(row)
    return O

#Calculating sum 

def sum(A,B):
    O = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        O.append(row)
    return O
    
    
m = int(input("Enter row\n"))
n = int(input("Enter column\n"))

print("Enter matrix A")
A = matrix(m,n)
print(A)
print("Enter matrix B")
B = matrix(m,n)
print(B)

print("Final Matrix")
result = sum(A,B)
print(result)