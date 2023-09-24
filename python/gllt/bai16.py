#import thu vien
import time
# time.time()
# time.ctime()
# time.sleep() so giay thuc thi lenh tiep theo
# time.localtime() tra ve thoi gian hien tai
giay=time.time()
print(giay)

hientai=time.ctime(time.time())
print(hientai)

print("moi nhap dap an :")
time.sleep(0)
print("het gio")

tg3 = time.localtime()
print(tg3)
print("nam hien tai la : ", tg3.tm_year)
print("thang hien tai la : ", tg3.tm_mon)
