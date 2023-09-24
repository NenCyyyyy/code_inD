sum = 0
for n in range(1,6,2):
    if n==3 :
       continue # continue break
    print("n = ", n)
    sum+=n
print(f"tong la sum = {sum}")