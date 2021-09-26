f = open("text1.txt", "r")
text = f.read()
f.close()
textDict = dict()
message = text.lower().replace("\n", "").replace("--", "").split()

for word in message:
    if word in textDict.keys():
        textDict[word] += 1
    else: textDict.update({word:1})
f = open("textDict.txt", "w+")
for word, number in textDict.items():
    f.write(word + ": " + str(number) + "\n")
f.close()
