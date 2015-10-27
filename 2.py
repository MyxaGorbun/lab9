def f(y, z):
    z = 1500/z
    z = 815 - z
    return (108 - z/y)
x0 = 4
x1 = 4.25
for i in range(28):
    x2 = f(x1, x0)
    x0 = x1
    x1 = x2
print(x2)