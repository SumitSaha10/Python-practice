#Program to check to palindrome number
def palindromeNumber(n):
	copy_n = n
	rev = 0
	while(copy_n>0):
		rem = copy_n % 10
		rev = rev * 10 + rem
		copy_n = copy_n // 10
	
	if(rev == n):
		print("Palindrome Number")
	else:
		print("Not a palindrome Number")

#Program to check to palindrome name
def palindromeString(name):
	name2 = name [::-1]
	name2 = name2.lower()
	name = name.lower()
	if(name == name2):
		print("Palindrome")
	else:
		print("Not Palindrome")



