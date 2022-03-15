num = str(input())
num2 = int(num, 16)+4294967296
if int(num2) >= 0:
    print((bin(num2))[3:])
else:
    num2 = 4294967296 + num2
    print((bin(num2))[3:])

