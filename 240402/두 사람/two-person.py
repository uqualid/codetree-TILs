a = input().split()
b = input().split()

a[0] = int(a[0])
b[0] = int(b[0])

if (a[0]>18 and a[1] == 'M') or (b[0]>18 and b[1] == 'M'):
    print("1")

else:
    print("0")