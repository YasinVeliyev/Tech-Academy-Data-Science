[*wardrobe, x, y] = [int(i) for i in input().split()]
wardrobe.sort()
if (wardrobe[0] <= x and wardrobe[1] <= y) or (wardrobe[1] <= x and wardrobe[0] <= y):
    print("YES")
else:
    print("NO")
