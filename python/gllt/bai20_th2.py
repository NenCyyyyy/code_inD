def roi(dt,cp):
    return (dt-cp)/cp
def Quyetdinhdautu(roi):
    if roi>=0.75 :
        return "dau tu la ro"
    else:
        return "dau cai cc"

print("ct tinh roi")
cp=float(input("nhap vao chi phi : "))
dt=float(input("nhap vao doanh thu : "))
roi=roi(dt,cp)
Qdtt= Quyetdinhdautu(roi)
print(Qdtt)
print(f"ti le roi la : {roi}")
