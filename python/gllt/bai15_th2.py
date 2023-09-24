n = int(input("nhap ao chieu cao : "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*", end="  ")
        else:
            print(" ",end="  ")
    print()
print("_"*50)
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i+j==n-1:
            print("*", end="  ")
        else:
            print(" ",end="  ")
    print()