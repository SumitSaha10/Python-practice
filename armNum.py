#Program to check Armstrong Number 
def armstrongNumber(n):
	n2 = 0
	copy_n = n
	digit = len(str(n))
	while(copy_n>0):
		rem = copy_n % 10
		n2 += rem ** digit
		copy_n = copy_n // 10
	if(n == n2):
		print(n," is a Armstrong Number")
	else:
		print(n," is not a Armstrong Number")

n = int(input("Enter number\n"))	
armstrongNumber(n)