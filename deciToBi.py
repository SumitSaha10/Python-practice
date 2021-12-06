#Program to convert decimal to binary
def deciToBi(n):
	binary = []
	
	while(n>0):
		rem = n%2
		binary.append(rem)
		n = n // 2
		
	binary.reverse()

	print(binary)

n = int(input("Enter decimal number\n"))
deciToBi(n)



