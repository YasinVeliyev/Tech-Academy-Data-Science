[end, start] = [int(i) for i in input().split()]

for i in range(end, start+1):
    odd = True
    num = i
    while num > 0:
        remainder = num % 10
        if remainder % 2 == 0:
            odd = False
            break
        num //= 10
    else:
        print(i, end=" ")
