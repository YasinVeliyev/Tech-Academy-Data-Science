n = int(input())
reverse = 0
while n > 0:
    reverse = reverse*10+n % 10
    n //= 10

nth = 0
even = 0
odd = 0

while reverse > 0:
    if nth % 2 == 0:
        odd += reverse % 10

    else:
        even += reverse % 10

    nth += 1
    reverse //= 10

print(odd*even)
