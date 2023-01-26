arr = [int(i) for i in input().split()]
m = arr[0]
for i in arr:
    if i > m:
        m = i
print(m)
