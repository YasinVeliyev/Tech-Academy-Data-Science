[h, w, l, k] = [int(i) for i in input().split()]
v = h*w*l
print((v//k + 1) if v % k else v//k)
