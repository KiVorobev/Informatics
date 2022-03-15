def shortener(st):
    while '(' in st or ')' in st:
        a = st.rfind('(')
        b = st.find(')', a)
        st = st.replace(st[a:b + 1], '')
    return st
st = str(input())
print(shortener(st))
