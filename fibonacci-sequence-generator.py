def fibo(y):
	y = int(y)
	l = [0]
	f0 = 0
	f1 = 1
	for n in range(0,y):
		l.append(f1)
		f1 = f0+f1
		f0 = f1-f0
		n+=1
	return l

def sum(*args):
	total = 0
	for x in args:
		total+=x
	return total

y = input("Up to what index do you want to list and sum the Fibonacci series? ")
print(f"The list up to the {y}. Fibonacci number is {fibo(y)} and the sum is {sum(*fibo(y))}")
