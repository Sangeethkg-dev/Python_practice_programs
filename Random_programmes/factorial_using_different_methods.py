
#factorial using for loop
"""
n=int(input("enter the number that you want the factorial of "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)
"""
#factorial using while loop
"""
n=int(input("Enter the number you want factorial of "))
factorial=1
c=0
while c<=n:
    c+=1
    factorial*=c
print(factorial)
"""
#factorial using recursion
"""
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number "))
print("Factorial of",num,"is",factorial(num))
"""