while True :
    hten= input("nhap vao ten : ")
    mhoc = input("nhap mon hoc : ")
    diem = float(input("nhap diem : "))
    print(f"ten : {hten} || mon thi : {mhoc} || so diem {diem}")
    if diem >=7 :
        print("xep loai diem : Dat")
    else:
        print("khong dat")
    hoi = input("nhap n de thoat, hoac bam bat ky de tiep tuc")
    if hoi== "n" or hoi == "N":
        break
