#@Author Ramkumar

#modules
import math
#taking variables
a= int(input(' Enter Value of a'))
b= int(input('Enter Value of b'))
c= int(input('Enter Value of c'))

#logic
#x = math.sqrt(c)
x = (-b+(math.sqrt(b**2)-(4*a*c)))/2*a
y = (-b-(math.sqrt(b**2)-(4*a*c)))/2*a
#dispalying the result
print('The Negative sqrt is',x)
print('The Positive sqrt is',y)
