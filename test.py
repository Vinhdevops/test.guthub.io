print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
a = input("Tên của bạn là gì")
print(a)
print(f"Chào mừng {a} đến với trò chơi")
print(f"Nhiệm vụ của {a} là tìm ra 1 kho báu")
luachon1 = input('bạn đang có 2 con đường đi phía trước bạn chọn "Trai" hay "Phai".').lower()
if luachon1 == "phai":
    luachon2 = input(f'Xin chúc mừng hero {a} đã vượt qua thử thách đầu tiên.Bây giờ bạn chọn "bangqua" hay "wait".').lower()
    if luachon2 == "wait":
        luachon3 = input('Bạn đã vượt ải thành công.Bây giờ trước mặt bạn là 3 cánh cổng có 3 màu khác nhau. Hãy chọn "đỏ","cam" or "vàng".').lower()
        if luachon3 == "đỏ":
            print("Thua rồi")
        elif luachon3 == "cam":
            print("thắng rồi")
        elif luachon3 == "vang":
            print("thua rồi")
        else :
            print("gõ sai rồi")
    else:
        print("Trò chơi kết thúc.Bạn đã thất bại")
else:
    print("Trò chơi kết thức vì bạn đã rơi vào một cái hố")
#