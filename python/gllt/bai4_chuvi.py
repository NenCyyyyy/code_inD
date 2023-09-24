import math
r = float(input("moi nhap vao ban kinh cua duong tron : "))
print(r)
cv = 2*r*math.pi
dt = r**2*math.pi
print("chu vi la : ",cv)
print("dien tich la : ", dt)
#in cach 2
print(f"chu vi hinh tron : {cv}")

print("cv la : ", cv, "dien tich la: ", dt)
print(f"cv la : {cv}, dt la : {dt}")
#cach3
print("chu vi la {}, dien tich la {}".format(cv,dt))

print(math.pi)