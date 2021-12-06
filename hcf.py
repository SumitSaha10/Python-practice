#Program to find LCM of two numbers
def hcf(num1,num2):
	minNum = min(num1,num2)
	for i in range(1,minNum+1):
		if(num1%i==0 and num2%i==0):
			hcf = i
	return hcf

n1 = int(input('Enter first number\n'))	
n2 = int(input('Enter second number\n'))	
result = hcf(n1,n2)
print(result)