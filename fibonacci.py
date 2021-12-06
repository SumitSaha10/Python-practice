#Program for fibonacci series
def fiboRec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiboRec(n-1)+fiboRec(n-2)

#Program for fibonacci series using recursion 
def fibo(n):
    prevNum =0
    currentNum =1
    for i in range(1,n):
        preprevNum = prevNum
        prevNum= currentNum
        currentNum = preprevNum + prevNum
    return currentNum
        
n = int(input('Enter number '))
print("The fibonacci recursion sum is ", fiboRec(n))
print("The fibonacci iterative sum is ", fibo(n))