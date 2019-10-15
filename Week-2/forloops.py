# find the sum of all the multiples of 3 and 5 for numbers under 100

total = 0

for n in range (1, 100):
    if n % 3 == 0 or n % 5 == 0:
        total = total + n

print(total)