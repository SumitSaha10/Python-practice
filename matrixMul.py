#Calculating Multiplication
def matrixMul(A,B):	
	C = []
	for i in range(0,len(A)):
		row = []
		for j in range(0,len(B[0])):
			cal =0
			for k in range(0,len(B)):
				cal += A[i][k] * B[k][j]
			row.append(cal)
		C.append(row)
	return C	
	
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
    
print("Enter matrix A")
m = int(input("Enter the value of row\n"))
n = int(input("Enter the value of column\n"))
A = matrix(m,n)

print("Enter matrix B")
m2 = int(input("Enter the value of row\n"))
n2 = int(input("Enter the value of column\n"))
B = []
if(n==m2):
	B = matrix(m,n)
else:
	print("Multiplication not possible")
	exit()
	
C = matrixMul(A,B)

print(C)