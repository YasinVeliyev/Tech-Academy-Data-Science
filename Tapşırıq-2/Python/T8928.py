number = int(input())

greatest = 1

if number % 2 == 0:
    greatest = number/2

elif number % 3 == 0:
    greatest = number/3
else:
    for i in range(5, int(number**0.5)+1, 6):
        if number % i == 0:
            greatest = number/i
            break
        elif number % (i+2) == 0:
            greatest = number / (i+2)
            break

print(int(greatest))
