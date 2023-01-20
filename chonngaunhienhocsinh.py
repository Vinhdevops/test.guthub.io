import random
dshs = input("Hãy nhập tên của học sinh vào hệ thống: ")
ten = dshs.split(", ")
tths = len(ten)
chonngaunhien = random.randint(0, tths - 1)
nguoilentrabai = ten[chonngaunhien]
print(f"Xin chúc mừng {nguoilentrabai} là người lên trả bài ")





