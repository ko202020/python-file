#중첩 for문
""" for dan in range(2,5):
    print(dan,"단")
    for num in range(1,10):
        print(f"{dan} x {num} = {dan*num}") """
""" *
**
***
****
*****
 ****
  ***
   **
    *

    *
   ***
  *****
 *******
********* """
#첫번째
a=int(input("몇층 찍을래?"))
b=" "
c="*"
for z in range(1,a+1):
    print(c*z,end='')
    for v in range(6-a):
        print(b,end='')
    print()
""" 
#두번째
a=int(input("몇층 찍을래?"))
b=" "
c="*"
for z in range (1,a+1):
    print(b*(z),end='')
    for x in range(5-z):
        print("*",end='')
    print()
#세번째
a=int(input("몇층 찍을래?"))
b=" "
c="*"
for z in range (1,a+1):
    print(b*(5-z),end='')
    for v in range(1,z*2):
        print(c,end='')
    print()
 """
