import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

#It evaluates the expression;

#you want to be absolutely safe from evidently wrong data

#secures your code from producing invalid results

#assertions don't supersede exceptions or validate the data - 
# they are their supplements.