import time

ten = input("nhap vao ten : ")
tuoi = int(input("nhap vao so tuoi : "))
htai = time.localtime()
nam=htai.tm_year
print(nam)
print(f"nam{ten} dat 100 tuoi la : {100-tuoi+nam}")
