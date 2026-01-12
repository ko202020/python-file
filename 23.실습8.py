""" import random
a =  random.radint (1,100)
print(a) """
import random
f=0
while True:
    x = input("1.게임시작 2.게임종료")#재할당
    if x == "1":
        print("게임을 시작합니다")
        a = random.randint(1,100)
        while True:
         c =int(input("값을맞춰주세요"))
         f+=1
         if c > a:
            print("정답은 더 작아요!")
         elif c< a:
            print("정답은 더 커요!")
         elif c==a:
            print(f"정답입니다! {a}이였고, 시도횟수는 {f}번 이었습니다")
            break    
    elif x == "2":
        print("게임을종료합니다")
        break
""" #내장/외장 라이브러리
#import random #내장 라이브러리
#업앤다운
56 input=40 56>40 "더 높게 입력해주세요!"
a=  random.radint(1,100)
print(a)
while True:
    if x == 1:
        print("게임시작합니다")
1. 값을 맞추면 '정답입니다! {}이였고, 시도횟수는{}번이였습니다'
2. 게임이 끝나면 > 메뉴 (1번 게임시작 2번 게임종료)
3. 2번 누르면 게임종료 """
