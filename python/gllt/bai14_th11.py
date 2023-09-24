# for i in range(1,51,1):
#     '''  if i%3==0 :
#         print(i,end=" ")'''
#     if i%3!=0:
#         continue
#     print(i, end=(" "))
m=1
sum=0
for i in range(1,11):
    m=i*m
    sum = sum + m
print(f"tong la {sum}")