#while문을 사용해서
# 1 을 누르면 "게임 시작"
# 2 를 누르면 "게임 종료" -> while 종료됨
""" a=input("게임시작할까요")
while True:
    if a== 1:
       print("게임시작")
    if a==2:
     break
print("게임 종료") """
while True:
    x = input("1.게임시작 2.게임종료")#재할당
    if x == "1":
        print("게임을 시작합니다")
    elif x == "2":
        print("게임을종료합니다")
        break