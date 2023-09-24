# t = int(input("nhap vao 1 thang bat ky tu 1 den 12 : "))
# if t in(1,2,3):
#     print(f"{t} thuoc quy 1")
# elif t in(4,5,6):
#     print(f"{t} thuoc quy 2")
# elif t in(7,8,9):
#     print(f"{t} thuoc quy 3")
# elif t in(10,11,12):
#     print(f"{t} thuoc quy 4")
# else:
#     print(f"lam deo gi co thang {t}")
from math import sqrt
a = int(input("nhap vao a ; "))
b = int(input("nhap vao b ; "))
c = int(input("nhap vao c ; "))
delta = (b**2)-4*a*c
if delta < 0:
    print("pt vo nghiem")
elif delta == 0 :
    print(f" nghiem kep {-b/(2*a)}")
else:
    print("pt co 2 nghiem pb : ")
    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)
    print(f"x1= {x1}, x2={x2}")

