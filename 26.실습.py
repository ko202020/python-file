import random
b =[]#로또번호
h =[]#이력
while True:
    x=input("1)추첨 2)이력보기 3)종료")#메뉴
    if x == "1":
        while True:
            s=input("1)자동추첨 2)수동추첨")
            if s == "1":
                b=[]
                while len(b)<6:
                 a = random.randint(1,45)
                 if a not in b:
                  b.append(a)
                  b.sort()
                print("추첨번호 :", *b)
                h.append(b)
                break
            elif s=="2":
               b=[]
               while len(b)<6:
                f=int(input("수동추첨을 위해 1부터45 사이의 숫자를 입력해주세요"))
                if f not in b:
                 b.append(f)
                 b.sort()
                 print(b)
               h.sort()
               h.append(b)
               print("수동추첨이 완료되었습니다 메뉴로 돌아갑니다")
            break
               
    elif x == "2":
        for i in range(len(h)):
            print(f"{i+1}회: ",end='')
            for j in range(i):
                print( h[i][0],h[i][1],h[i][2],h[i][3],h[i][4],h[i][5])
                print()
    elif x == "3":
        break
    

""" 
a = random.randiant(1,45)
b.append(a)
if a not in b : #포함 되어있다면
    b.append(a) """

