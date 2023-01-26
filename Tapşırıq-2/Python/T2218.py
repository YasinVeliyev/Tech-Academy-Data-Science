count = int(input())

zero = 0
one = 0

while count > 0:
    count -= 1
    coin = int(input())
    if coin == 0:
        zero += 1
    else:
        one += 1

print(zero if zero < one else one)
