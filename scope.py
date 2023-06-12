
def func(y):
    global x
    x += 1
    y += 1
    print(x)
    print(y)

x = 10
y = 20
print(x)
print(y)
func(y)
print(x)
print(y)

