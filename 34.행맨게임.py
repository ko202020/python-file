#game2
import random
import time
import os
fruit=["apple","banana","melon","orange","grape","strawberry","watermelon","pineapple","peach",]
animal=["dog","cat","lion","tiger","elephant","giraffe","monkey","rabbit","bear","zebra"]
sports=["soccer","baseball","basketball","tennis","golf","volleyball","swimming","boxing","cycling","badminton"]
rank=[]
filename = "hangman_ranking.txt"
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
def make_hint(answer, alphabet):
    hint = ""
    for x in answer:
        if x in alphabet:
            hint += x 
        else:
            hint +="_"
    return hint
def hangman_game():
    while True:
        fas={1:fruit,2:animal,3:sports}
        try : level=int(input("1.과일 2.동물 3.스포츠"))
        except :
            print("숫자를 눌러주세요")
            continue
        chance=10
        alphabet=[]
        if level in fas:
            print("게임을 시작하겠습니다")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            answer = random.choice(fas[level])
            tries=0
            while chance>0:
                hangman=(input("단어를 입력해주세요")).strip().lower()
                if len(hangman)==1:
                    if hangman in answer and hangman not in alphabet:
                        alphabet.append(hangman)
                        hint=make_hint(answer, alphabet)
                        print(hint)
                        if "_" not in hint:
                                    print("정답입니다")
                                    name=(input("랭킹등록을 위해 닉네임을 입력해주세요"))
                                    rank.append([tries,name])
                                    g = open(filename, "a", encoding="utf-8")
                                    g.write(f"{tries},{name}\n")
                                    g.close()
                                    return
                    elif hangman in alphabet:
                        print("이미 입력한 글자입니다")
                    else:
                        chance-=1
                        tries+=1
                        print(f"오답입니다 횟수 1회 차감! 남음 기회는{chance}")
                        hint=make_hint(answer, alphabet)
                        print(hint)
                else:
                    print("한글자만 입력하세요")
                if chance==0:
                    print("게임에 실패했습니다. 메뉴로 돌아갑니다")
                    return
def super():
    while True:
        try:super=int(input("1.랭킹 초기화"))#관리자모드메뉴
        except :#에러제거
            print("숫자만 입력해주세요")
            continue
        if super == 1:#랭킹초기화
            try:password=int((input("비밀번호를 입력해주세요")))
            except:
                print("비밀번호는 숫자입니다")
                continue
            if password==1234:
                rank.clear()
                target = os.path.join("hangman_ranking.txt")
                if os.path.exists(target):
                    os.remove(target)
                return
def game2():
    while True:    
        try:menu=int(input("1.게임시작 2.랭킹보기 3.관리자모드"))
        except:
            print("숫자를 눌러주세요")
            continue
        if menu==1:
            hangman_game()
        elif menu==2:
            rank.sort()
            show_rank()
        elif menu==3:
            super()
while True:#본게임
    game2()
        