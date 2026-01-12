#리스트 1차원 2차원
#딕셔너리
person = {"name1":"홍길동","age":22,"s":[1,2,3]} #이름:값 키:값
print(person)
print(person["s"])
print(type(person["s"]))
""" [22,2000,170]
나이,학번,키,몸무게 """
student={"name":"홍길동","age":20,"grade":3}
print("이름 :",student["name"])

person["name1"]="김병철"
person["이름"]="김병철"
person["age"]="김병철"
print(person) 

for k in person:
    print(k)
    print(person[k])

#여러학생정보관리
students = [{"name":"민수","score":80},
    {"name":"성민","score":60},
    {"name":"은혁","score":70}]

""" for s in students: 
    print(s["name"],s["score"])
for s in students: 
    total +=s["score"]
total =0
for s in students :#리스트반복문 s ={"name":"은혁","score":70}
    total += s["score"]
print('평균 점수:',total/len(students))
student={"name":"홍길동","age":20,"grade":3}
if student["grade"]>=3:
    student["result"]="우수 학생"
else:
    student["result"]="보통 학생" """
print(student)
#keys/values/items 자주사용
#student ={"name":"홍길동","age":20,"grade":3}
print(person.key())
print(person.values())
print(person.items())

for k, v in person.items():#('name1','김병철')
    print(k,v)
#딕셔너리 메서드
print(person.get("age"))
print(person.get("name1"))
print(person.get("age","-"))
print(person)
#값 추가/갱신
print(person.update("name1")({"age":22,"city":"seoul"}))
print(person)
#값 삭제1 -휴지통
a = person.pop("s")
print(a)
print(person)
#값 삭제2-완전삭제
del person["이름"]
print(person)

#마지막 요소 삭제 -popitem()
k,v = person.popitem()
print(k,v)
print(person)
#전체 삭제 clear()
person.clear()
print(len(person))