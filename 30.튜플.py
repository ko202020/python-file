#튜플
#()
t=(10,20,30)#튜플
print(t)

t2 = 10,20,30 #튜플
print(type(t2))

t3 = (10, )
print(t[0],t[1],t[2])
#t[0] =30 #Error 불변 자료형 박물관의 전시품이나 다름없어서 고정돼있음

for x in t:
    print(x)
#슬라이싱
print(t[1:4])
#튜플 메서드
#count()
print(t.count(20))
#index()
print(t.count(20))
t=(10,20,30)
a,b,c=t
print(a,b,c)