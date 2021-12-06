#Program to find HCF of two numbers
def lcm(num1,num2):
	maxNum = max(num1,num2)
	while True:
		if(maxNum%num1==0 and maxNum%num2==0):
			lcm = maxNum
			return lcm
		maxNum+=1

n1 = int(input('Enter first number\n'))	
n2 = int(input('Enter second number\n'))
result = lcm(n1,n2)
print(result)
			