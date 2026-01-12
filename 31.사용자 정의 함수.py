#사용자 정의함수 def
def show_students():
    print("학생 목록 출력")
    print("kim - 90점")
    print("lee-80점")

show_students()
show_students()
#조건
#1. 2번 이상 반복이 된다
#2. while / if 구조 자체가 반복이 된다.
#3. 한 함수가 입력/처리/출력 ->나누기
a = 2
#4. 한 번 고치면 여러 곳을 고쳐야 한다.

#def 함수이름(매개변수):
    #실행할 코드
    
""" def add(a,b):    # a b 는 매개변수
    return a + b # 연산을 하고, 가지고 있는다. -> 반환(돌려준다)
print(add(3,4))  #인자 인수
print(add(23,34)) """

def add(a,b="안녕하세요"):
    print(b,a)
print(add(a))
#가변인자
def total(*args): # a b 는 매개변수
    print(args)
total(1,2,3,4) #튜플 - 변하지 않는

def sum_all(*nums):
    total = 0
    for n in nums:
        total +=n
    return total
print(sum_all(1,2,3,4,5))

#가변 딕셔너리
def show_info(**kwargs):
    print(kwargs)

def show_info(**info):
    for k, v in info.items():
        print(k, ":", v)
show_info(name="kim",score=80, grade="c")

def example(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
example(1,2,3,4,name="김찬영")
        