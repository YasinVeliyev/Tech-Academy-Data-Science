import math
[r, w, l] = [int(i) for i in input().split()]

print("YES" if math.sqrt(r**2-(w/2)**2)*2 >= l else "NO")
