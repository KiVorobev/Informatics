def compress(uncompressed):
    dict_size = 256
    dictionary = dict((chr(i), chr(i)) for i in range(dict_size))

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result



def decompress(compressed):
    dict_size = 256
    dictionary = dict((chr(i), chr(i)) for i in range(dict_size))


    w = result = compressed.pop(0)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result

fileInn = open('fileIn.txt')
fileIn = fileInn.read()
fileInn.close()
fileOut = open('FileOut.txt', 'a')

try:
    compressed = compress(fileIn)
    fileOut.write(str(compressed))
    decompressed = decompress(compressed)
    fileOut.write(str(decompressed))
    print('True')
except:
    print('False')
finally:
    print('Program was completed')
