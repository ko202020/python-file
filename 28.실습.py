""" import random
a= random.choice(c)
c=["가위","바위","보"]
print(a)
#사용자가 입력을 하면 입력한 값과 랜덤으로 나온 값과 비교해서
#승 패를 만듭니다
#1. 게임시작
#2. 단일게임
#심화3. 묵찌빠
#2. 게임 종료
 """
import random
c=["가위","바위","보"]
mjp=["묵","찌","빠"]
while True:
    x=input("1.게임시작 2.게임종료")
    if x=="1":
        x=input("1.3판 2선승제, 2.단판승부, 3.묵찌빠")
        f=0
        b=0
  
        if x=="1":
            while True:
             z=input("1.가위 2.바위 3.보")
             a= random.choice(c)
             if z=="1":
                if a=="가위":
                    print("나 : 가위 vs 알파고 : 가위")
                    print("무승부")
                elif a=="바위":
                    print("나 : 가위 vs 알파고 : 바위")
                    print("패배")
                    f+=1
                    b-=1
                    
                elif a=="보":
                    print("나 : 가위 vs 알파고 : 보")
                    print("승리")
                    f+=1
                    b+=1
                if b>1:
                    print("승리하였습니다")
                    break
                elif b==-2:
                    print("패배하였습니다")
                    break
                elif f==3:
                    if b>0:
                        print("승리하였습니다")
                        break
                    if b<0:
                        print("패배하였습니다")
                        break
             if z=="2":
                if a=="바위":
                    print("나 : 바위 vs 알파고 : 바위")
                    print("무승부")
                elif a=="보":
                    print("나 : 바위 vs 알파고 : 보")
                    print("패배")
                    f+=1
                    b-=1
                    
                elif a=="가위":
                    print("나 : 바위 vs 알파고 : 가위")
                    print("승리")
                    f+=1
                    b+=1
                if b>1:
                    print("승리하였습니다")
                    break
                elif b==-2:
                    print("패배하였습니다")
                    break
                elif f==3:
                    if b>0:
                        print("승리하였습니다")
                        break
                    if b<0:
                        print("패배하였습니다")
                        break            
             if z=="3":
                if a=="보":
                    print("나 : 보 vs 알파고 : 보")
                    print("무승부")
                elif a=="가위":
                    print("나 : 보 vs 알파고 : 가위")
                    print("패배")
                    f+=1
                    b-=1
                    
                elif a=="바위":
                    print("나 : 보 vs 알파고 : 바위")
                    print("승리")
                    f+=1
                    b+=1
                if b>1:
                    print("승리하였습니다")
                    break
                elif b==-2:
                    print("패배하였습니다")
                    break
                elif f==3:
                    if b>0:
                        print("승리하였습니다")
                        break
                    if b<0:
                        print("패배하였습니다")
                        break
        if x=="2":
            while True:
                z=input("1.가위 2.바위 3.보")
                a= random.choice(c)
                if z=="1":
                 if a=="가위":
                    print("나 : 가위 vs 알파고 : 가위")
                    print("무승부")
                 elif a=="바위":
                    print("나 : 가위 vs 알파고 : 바위")
                    print("패배")
                    break
                 elif a=="보":
                    print("나 : 가위 vs 알파고 : 보")
                    print("승리")
                    break
                if z=="2":
                 if a=="바위":
                    print("나 : 바위 vs 알파고 : 바위")
                    print("무승부")
                 elif a=="보":
                    print("나 : 바위 vs 알파고 : 보")
                    print("패배")
                    break
                 elif a=="가위":
                    print("나 : 바위 vs 알파고 : 가위")
                    print("승리")
                    break
                if z=="3":
                 if a=="보":
                    print("나 : 보 vs 알파고 : 보")
                    print("무승부")
                 elif a=="가위":
                    print("나 : 보 vs 알파고 : 주먹")
                    print("패배")
                    break
                 elif a=="바위":
                    print("나 : 보 vs 알파고 : 바위")
                    print("승리")
                    break
        if x=="3":
            f=0
            while True:
                z=input("1.가위 2.바위 3.보")
                a= random.choice(c)
                if z=="1":
                 if a=="가위":
                    print("나 : 가위 vs 알파고 : 가위")
                    print("무승부")
                 elif a=="바위":
                    print("나 : 가위 vs 알파고 : 바위")
                    print("패배")
                    f-=1
                 elif a=="보":
                    print("나 : 가위 vs 알파고 : 보")
                    print("승리")
                    f+=1
                 if f==1:
                   while True:
                      z=input("1.묵 2.찌 3.빠")
                 if f==2:
                   while True:
                      z=input("1.묵 2.찌 3.빠")

                      

                            