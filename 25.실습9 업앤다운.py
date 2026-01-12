def game():
    rank=[]
    import random
    while True:
        x = input("1.게임시작 2.랭킹 보기 3.도움말 4.관리자모드 5.게임종료")#메뉴
        if x == "1":
            while True:
             e = input("1.쉬움 1~50 2.보통 1~100 3.어려움 1~500")
             if e == "1":
                print("게임을 시작합니다")
                a = random.randint(1,50)
                f=0
                while True:
                    c =int(input("값을맞춰주세요"))
                    f+=1
                    if c > a:
                     print("정답은 더 작아요!")
                    if f==3:
                        if a%2==0:
                            print("힌트! 정답은 짝수!")
                        if a%2==1:
                            print("힌트! 정답은 홀수!")
                    if f==5:
                        c=input("힌트를 보시겠습니까? y or n")
                        if c=="y":
                            if a>25:
                                print("힌트 정답은 25~50 ")
                            elif a<25:
                                print("힌트 정답은 1~24")                                                                         
                    elif c< a:
                        print("정답은 더 커요!")
                        if f==3:
                         if a%2==0:
                            print("힌트! 정답은 짝수!")
                         if a%2==1:
                            print("힌트! 정답은 홀수!")
                        if f==5:
                         c=input("힌트를 보시겠습니까? y or n")
                        if c=="y":
                            if a>25:
                                print("힌트 정답은 25~50 ")
                            elif a<25:
                                print("힌트 정답은 1~24")
                    elif c==a:
                        print(f"정답입니다! {a}이였고, 시도횟수는 {f}번 이었습니다")
                        v=input("이름을 입력하세요")
                        rank.append ([f,v])
                        yn=input("더 진행 하시겠습니까? y or n")
                        if yn == "y":
                            print("난이도 선택으로 돌아갑니다")
                            break
                        if yn == "n":
                            print("메뉴로 돌아갑니다")
                            break
                if yn == "n":
                    break
             elif e == "2":
                print("게임을 시작합니다")
                a = random.randint(1,100)
                f=0
                while True:
                    c =int(input("값을맞춰주세요"))
                    f+=1
                    if c > a:
                     print("정답은 더 작아요!")
                    if f==3:
                        if a%2==0:
                            print("힌트! 정답은 짝수!")
                        if a%2==1:
                            print("힌트! 정답은 홀수!")
                    if f==5:
                        c=input("힌트를 보시겠습니까? y or n")
                        if c=="y":
                            if a>50:
                                print("힌트 정답은 50~100")
                            elif a<51:
                                print("힌트 정답은 1~50")
                    elif c< a:
                        print("정답은 더 커요!")
                        if f==3:
                         if a%2==0:
                            print("힌트! 정답은 짝수!")
                         if a%2==1:
                            print("힌트! 정답은 홀수!")
                        if f==5:
                         c=input("힌트를 보시겠습니까? y or n")
                        if c=="y":
                            if a>50:
                                print("힌트 정답은 51~100 ")
                            elif a<51:
                                print("힌트 정답은 1~50")
                    elif c==a:
                        print(f"정답입니다! {a}이였고, 시도횟수는 {f}번 이었습니다")
                        v=input("이름을 입력하세요")
                        rank.append ([f,v])
                        yn=input("더 진행 하시겠습니까? y or n")
                        if yn == "y":
                            print("난이도 선택으로 돌아갑니다")
                            break
                        if yn == "n":
                            print("메뉴로 돌아갑니다")
                            break
                if yn == "n":
                    break
                
             elif e == "3":
                print("게임을 시작합니다")
                a = random.randint(1,500)
                f=0
                while True:
                    c =int(input("값을맞춰주세요"))
                    f+=1
                    if c > a:
                     print("정답은 더 작아요!")
                    if f==3:
                        if a%2==0:
                            print("힌트! 정답은 짝수!")
                        if a%2==1:
                            print("힌트! 정답은 홀수!")
                    if f==5:
                        c=input("힌트를 보시겠습니까? y or n")
                        if c=="y":
                            if a>250:
                                print("힌트 정답은 251~500 ")
                            elif a<51:
                                print("힌트 정답은 1~250")
                    elif c< a:
                        print("정답은 더 커요!")
                        if f==3:
                         if a%2==0:
                            print("힌트! 정답은 짝수!")
                        if a%2==1:
                            print("힌트! 정답은 홀수!")
                        if f==5:
                         c=input("힌트를 보시겠습니까? y or n")
                        if c=="y":
                            if a>250:
                                print("힌트 정답은 251~500 ")
                            elif a<251:
                                print("힌트 정답은 1~250")
                    elif c==a:
                        print(f"정답입니다! {a}이였고, 시도횟수는 {f}번 이었습니다")
                        v=input("이름을 입력하세요")
                        rank.append ([f,v])
                        yn=input("더 진행 하시겠습니까? y or n")
                        if yn == "y":
                            print("난이도 선택으로 돌아갑니다")
                            break
                        if yn == "n":
                            print("메뉴로 돌아갑니다")
                            break
                if yn == "n":
                    break
        elif x == "2":#랭킹보기
            rank.sort(reverse=False)
            print("--명예의전당--")
            for i in range (len(rank)):
                print(f"{i+1}위 {rank[i][1]} {rank[i][0]}회")
                if i == 4:
                    break    
        elif x == "5":
            print("게임을종료합니다")
            break
        elif x == "3":
            print("숫자를 맞추는 게임입니다 열심히 찾아봅시다!")
            print("개발자 후원 계좌 번호 1234-1234-1234 하나은행")
        elif x == "4":
            while True:
                c=int(input("1.랭킹 초기화 2. 이름 변경"))
                if c == 1:
                    rank.clear()
                    break
                elif c == 2:
                    print("--명예의전당--")
                    for i in range (len(rank)):
                        print(f"{i+1}위 {rank[i][1]} {rank[i][0]}회")
                        if i == 4:
                            break
                    v=int(input("몇등의 이름을 변경하시겠습니까? 1~5까지의 숫자를 입력해주세요"))
                    rank[v-1][1]=input("변경할 이름을 입력해주세요")
                    break
gamestart=int(input("1.업앤다운 게임을 시작하시겠습니까?"))
if gamestart==1:
    game()