#반복문
""" for 변수 in 반복횟수:
    print(변수) """
""" for i in range(6): # 0 1 2 3 4 
    print(i)
#문자 자체를 반복하는 for문
for i in range(5): #0 1 2 3 4
    print(f"{i+1}위 입니다")
for i in range(1,6): #0 1 2 3 4, # 1은 시작이어서 출력 엔드는 안나옴
    print(f"{i}위 입니다") """
    #300400500
""" for i in range(3):
    print(i*100+300, end='')
""" for i in range(3,6):
    print(i*100, end='') """
for i in range(1,6,2): #(start, end, step)
    print(i)#1+step
# step 3의 배수 100까지만 출력하는 코드를 작성해보기
# step 사용하지 않고,if를 사용한3의 배수출력하기
for i in range(3,100,3):
    print(i)
for i in range(1,100):
    if i%3==0:
        print(i,end=' ') """

*
**
***
****
""" *****
층수=int(input("몇 층 찍으실건가요"))
for i in range(층수):
    print(층수*"*")
#for문은 무조건 1개만 / input("몇 층 찍으실껀가요") """
*****
 ****
  ***
   **
    *

    *
   ***
  *****
 *******
*********
a=int(input("층수"))
for i in range (a+1):
  print((" "*(5-i))+("*"(i*2-1)))