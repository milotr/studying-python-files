def isPrime(num):
    y = []
    for i in range(2,num):
        x = num % i
        y.append(x)
    if 0 not in y:
        print("Prime number:", end=" ")
        return num


for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1)