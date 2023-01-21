row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "0"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
luachon = input("nhập vào hàng cột mà bạn muốn chọn: ")
chonhangdoc = int(luachon[1])
chonhangngang = int(luachon[0])
hn = map[chonhangngang - 1]
print(hn[chonhangdoc-1])
