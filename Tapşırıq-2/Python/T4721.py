number = int(input())

count = 0

while number > 0:
    if number % 10 == 5:
        count += 1
    number //= 10
print(count)
