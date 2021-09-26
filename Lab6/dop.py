import itertools

def XOR_cipher(string, key):
    ans = []
    #using key for encryption str
    key = itertools.cycle(key)
    for s,k in zip(string, key):
        #application XOR
        ans.append(chr(ord(s) ^ ord(k)))
    return ''.join(ans)

def XOR_uncipher(string, key):
    ans = []
    #using key for encryption str
    key = itertools.cycle(key)
    for s,k in zip(string, key):
        #application XOR
        ans.append(chr(ord(s) ^ ord(k)))
    return ''.join(ans)

stroka1 = str(input('Введите строку: '))
print('Исходная строка: ', stroka1)
stroka2 = str(input('Введите ключ: '))
stroka3 = XOR_cipher(stroka1, stroka2)
print('Закодированная строка: ', XOR_cipher(stroka1, stroka2))
print('Раскодированная строка: ', XOR_uncipher(stroka3, stroka2))
