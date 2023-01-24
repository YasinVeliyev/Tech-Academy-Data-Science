month = int(input())

if month == 12 or month <= 2:
    print("Winter")
elif month >= 2 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
else:
    print("Autumn")
