# Sum even numbers between 1 and 100 (inclusive)

total = 0

for value in range(0, 101, 2):
	total += value


print(total)

total = 0

for value in range(1, 101):
	if (value % 2 == 0):
		total += value


print(total)	
