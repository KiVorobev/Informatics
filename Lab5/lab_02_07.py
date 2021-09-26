num = str(input())
dec = int(num, 12)
znak=0
if dec<0:
    dec*=-1
    znak=1
res = ''
cel = dec
while cel != 0:
    cel = dec // 14
    ost = dec % 14
    if ost > 9:
        if ost == 10:
            ost = 'A'
        if ost == 11:
            ost = 'B'
        if ost == 12:
            ost = 'C'
        if ost == 13:
            ost = 'D'
    res += str(ost)
    dec = cel
if znak==1:
    res += "-"
print(res[::-1])
