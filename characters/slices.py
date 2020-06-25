# Slices

alpha = "abdefg"

print(alpha[1:3]) #doesn't actually included #3 character
print(alpha[3:]) #all the way to the end
print(alpha[:3]) #doesn't actually included #3 character
print(alpha[3:-2]) #doesn't actually included #3 character
print(alpha[-3:4]) #THE SAME SINGLE CHARACTER
print(alpha[::2]) #jump iteration
print(alpha[1::2]) #starts at jump iteration