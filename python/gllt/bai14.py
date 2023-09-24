# for i in range(2,10,2) :
#     print("i = ", i)
a = int(input("nhap a : "))
n =int(input("nhap vao n : "))
if a%2==0 :
    for i in range(1,n,1):
        print(i)
        a+=i
    print("tong a la {}".format(a))
else:
    print("lam deo gi tinh tong le !")

