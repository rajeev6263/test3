
import math

# taking input from user
name  = input('what is your name' )

a = int(input("Enter a first number\n"))
b = int(input("Enter a second number\n"))

#implementing math functions
sub= a-b
add= a+b
mul = a*b
div = a/b
f = math.factorial(a)

#printing Results
print('Hello' ,name,' Please find below your calculations.')
print('Addition:', add )
print('subtraction:',sub)
print('Multiplication:', mul)
print('Division: ',div)
print('Factorial:', f)
print()	
print('Bye, see you next time')

