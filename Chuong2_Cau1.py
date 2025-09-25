# Cau 1: Tinh chu vi dien tich hinh tron
'''
De bai: Nhập bán kính đường tròn r. Tính và xuất chu vi, diện tích đường tròn tương ứng.
HD: cv=2*π*r và dt=π*r*r
'''
import math
try:
 r=float(input("Mời bạn nhập bán kính hình tròn:"))
 cv=2*math.pi*r
 dt=r**2
 print("Chu vi =",cv)
 print("Diện tích=",dt)
except:
 print("Lỗi rồi!")