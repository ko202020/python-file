rank=[]#랭킹 전역변수
import random#랜덤값라이브러리
import os
import time
filename = "ranking.txt"
rank = []
if not os.path.exists(filename):
    open(filename, "w", encoding="utf-8").close()
file = open(filename, "r", encoding="utf-8")
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip()  # 줄 끝 개행 제거
    if line == "":
        continue

    parts = line.split(",")   # ["3", "철수"]
    if len(parts) != 2:
        continue

    tries_str = parts[0].strip()
    name = parts[1].strip()

    # tries가 숫자인지 간단히 확인
    if tries_str.isdigit():
        tries = int(tries_str)
        rank.append([tries, name])

def show_rank():#랭킹보여주기(5등까지)
    print("--명예의전당 상위5인--")
    for i in range (len(rank)):#1위부터 5위까지의 랭킹과 시행횟수
        print(f"{i+1}위 {rank[i][1]} {rank[i][0]}회")
        if i == 4:#5등에서 멈추기
            break    
def level(difficulty):#난이도 설정 사용자정의함수
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    print("게임을 시작합니다")
    a = random.randint(1,difficulty)#난이도를 difficulty까지 랜덤으로 지정
    f=0#시행횟수
    while True:
        try:c =int(input("값을맞춰주세요"))#정답작성란
        except :#오류시 출력
            print("숫자를 입력해주세요")
            continue
        f+=1#틀릴때마다 시행횟수 증가
        if c==a:#정답일때
            print(f"정답입니다! {a}이였고, 시도횟수는 {f}번 이었습니다")#시행횟수와 정답출력
            v=input("이름을 입력하세요")#랭킹이름등록
            rank.append ([f,v])#랭킹에 이름과 시행횟수 추가
            g = open(filename, "a", encoding="utf-8")
            g.write(f"{f},{v}\n")
            g.close()
            while True:
                yn=input("더 진행 하시겠습니까? y or n")#게임재시작 선택
                if yn.lower() == "y":#재시작
                    return "다시"
                elif yn.lower()=="n":#초기메뉴
                    print("초기메뉴로 돌아갑니다")
                    return "메뉴"
        elif c>a:#정답이 더 작을때
            print("정답은 더 작아요!")
        else:#정답이 더 클때
            print("정답은 더 커요!")
        if f == 3:# 3회차 힌트
            if a % 2 == 0:#짝수
                print("힌트! 정답은 짝수!") 
            else:#홀수
                print("힌트! 정답은 홀수!")
        if f == 5:# 5회차 힌트
            hint = input("힌트를 보시겠습니까? y or n: ").strip().lower()#힌트볼지 선택, 대소문자 띄어쓰기 방지
            if hint == "y":#y일때 힌트출력방식
                mid = difficulty // 2#중간값
                if a > mid:#정답이 중간보다 클때
                    print(f"힌트 정답은 {mid}~{difficulty}")
                else:#정답이 중간보다 작을때
                    print(f"힌트 정답은 1~{mid-1}")
def game_choice():#난이도선택
        difficulty_map = {#난이도 리스트
            1: 50,
            2: 100,
            3: 250}
        while True:
            try:level_menu = int(input("1.쉬움 1~50 2.보통 1~100 3.어려움 1~500"))#난이도메뉴
            except :#에러방지
                print("1~3중에 선택해주세요")
                continue
            if level_menu in difficulty_map:#1~3난이도가 들어가면서 난이도리스트의 값 부분 출력해서 난이도 설정
                yesorno=level(difficulty_map[level_menu])
                if yesorno=="메뉴":#게임이 n선택을 통해 메뉴값으로 받아진다면 초기메뉴로 돌아감
                    return
            else:
                print("1~3중에 선택해주세요")
def game1():#업앤다운 게임
    while True:
        try : menu = int(input("1.게임시작 2.랭킹 보기 3.도움말 4.관리자모드 5.게임종료"))#메뉴
        except ValueError:#에러제거
            print("숫자를 눌러주세요")
            continue       
        if menu == 1:#게임시작
            game_choice()
        elif menu == 2:#랭킹보기
            rank.sort(reverse=False)
            show_rank()  
        elif menu == 5:#게임종료
            print("게임을종료합니다")
            break
        elif menu == 3:#도움말
            print("숫자를 맞추는 게임입니다 열심히 찾아봅시다!")
            print("개발자 후원 계좌 번호 1234-1234-1234 하나은행")
        elif menu == 4:#관리자모드
            while True:
                try:super=int(input("1.랭킹 초기화 2. 이름 변경"))#관리자모드메뉴
                except ValueError:#에러제거
                    print("숫자만 입력해주세요")
                    continue
                if super == 1:#랭킹초기화
                    rank.clear()
                    target = os.path.join("ranking.txt")
                    if os.path.exists(target):
                        os.remove(target)
                    break
                elif super == 2:#이름변경
                    rank.sort()
                    show_rank()#랭킹보여주기
                    name_change=int(input("몇등의 이름을 변경하시겠습니까? 1~5까지의 숫자를 입력해주세요"))#변경할 랭킹번호
                    rank[name_change-1][1]=input("변경할 이름을 입력해주세요")#변경되는 이름
                    break
                else:
                    continue
while True:
    try:gamestart=int(input("1.업앤다운 게임을 시작하시겠습니까? 2.게임종료"))#게임시작메뉴
    except ValueError:
        print("숫자를 입력해주세요")#오류 방지
        continue
    if gamestart==1:#게임시작
       game1()
    elif gamestart==2:#게임종료
       break
    else:
        continue
