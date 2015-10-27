e = 0.1
x = 0.1 * e
while 1 + x != 1:
    e = x
    x = 0.1 * e
if 1 + e != 1:
    print(e)