a = input()
b = '('
c = ')'
d = 0
e = 0
n = 0
o = 0
if a.count(b) > a.count(c):
    o = a.rfind(b)
    n = 1
for i in range(len(a)):
    if a[i] == b:
        d += 1
    if a[i] == c:
        e += 1
    if e > d:
        n = 1
        o = i
        break
if n == 1:
    print(o)
else:
    print('YES')
