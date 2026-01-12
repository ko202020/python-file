#전역변수 / 지역변수
import random
#def game()#먼저 선언해주기
 #   n = 0 #지역변수 def 안에서만 사용 가능
 #   return n

c=0 #전역변수
n=0 #전역변수
x=10#전역
def func():
    y=5#지역
    print(x)
    print(y)
    return y

def func1():
    return x+1
func1() 
#immutable(변경할수없는)vsmutable(변경할수있는)
#immutable
#숫자, 문자, 튜플
#mutable
#리스트, 딕셔너리, 셋
data1 = {"x":10}
def func3(s):
    s["x"]+=1
func3(data1)
print(data1)

#원본 유지 o
data2={"x":10}
def func4(s):
    data3 = s.copy()
    data3["x"]+=1
    return data3
new_data = func4(data2)
print(data2)     #원본
print(new_data)  #수정본