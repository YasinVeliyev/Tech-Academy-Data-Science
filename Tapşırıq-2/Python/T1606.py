number = int(input())

last = True
lastNumber = 0

if number < 0:
    number *= -1

while number >= 10:
    if last:
        lastNumber = number % 10
        last = False
    number //= 10

print(number+lastNumber)
