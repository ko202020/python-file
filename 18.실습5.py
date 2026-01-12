#구구단
#for문 연산을 위해서 작성하고...
#input을 통해서 몇 단 입력할까요?
#출력
#2 x 1 = 2
a=int(input("몇단 입력할까요?"))
""" for i in range (1,10):
    print(a,"x",i,"=",a*i) """
for i in range (1,10):
    print(f"{a} x {i} = {a*i}")