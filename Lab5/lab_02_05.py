text = set()
def rec(s, res):
    global text
    text.add(res)
    if len(s) >  0:
        for i in range(len(s)):
            rec(s[:i] + s[i + 1:], res + s[i])
my_str = input()
rec(my_str, "")
text.remove("")
print(*text)
