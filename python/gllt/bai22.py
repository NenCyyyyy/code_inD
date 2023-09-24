a=5
def test():
    global a
    a=200
    print(a)
print(a)
test()
print(a)  