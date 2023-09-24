dtb = float(input("nhap vao diem tb cho tao "))
if dtb >= 9.0 :
    print("gioi: ", dtb)
elif dtb>7.0 and dtb <9.0:
    print(f"thang nay kha : {dtb}")
elif dtb<7.0 and dtb>5.0:
    print("tau dam {}".format(dtb))
else:
    print("dup !", dtb)