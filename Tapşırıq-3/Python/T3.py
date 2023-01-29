n = int(input())
count = 0


def print_(start_and_end="+"):
    print(start_and_end, end=" ")
    for i in range(0, n-2):
        print("-", end=" ")
    print(start_and_end)


print_()
for i in range(n-2):
    print_("|")
print_()
