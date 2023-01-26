number = int(input())

product = 1
while number > 0:
    if number % 10 != 0:
        product *= number % 10
    number //= 10
print(product)
