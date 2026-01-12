""" """ #자료구조 - 리스트/튜플/딕셔너리/셋 #제일 많이 쓰는건 리스트 딕셔너리
nums = [1,2,3] #리스트 : 순서가 있고, 값을 바꿀 수 있다.
num = (1,2,3) #튜플 : 순서가 있지만, 값을 바꿀 수는 없다.
person = {"name1:김병철","name2:김병철"} #딕셔너리 : 이름:값(키:값)
#설명서같은 데이터 이다
u = {1,2,3} #셋 : 중복을 허용하지 않는 구조입니다.
#중복 제거용으로 많이들 사용한다


#리스트
nums = [1,2,3] #0부터 시작
print(nums[1])#2
print(nums[2])#3 인덱스번호
nums[2] = 25
#값 변경
print(nums)
nums2=[34,23,78]
print(nums*3)
print(type(nums))
#구조 변경
for n in nums2:
    print(n*3)
#구조 변경 - 리스트 반복문
for n in range(len(nums2)):#3 012
    print(n*4) """
#리스트 슬라이싱
nums = [10,20,30,40,50]
print(nums[1:4])#1부터 4 되기 전까지 나옴 #range
print(nums[:4])
print(nums[2:])
print(nums[::2])
print(nums[::-1])

scores = [70, 75, 65, 43, 14]
r_scores = scores[-3:]
print(r_scores)

#리스트 메서드 - 도구, 방법
#리스트.메서드()
nums = []
#nums = 0
nums.append("김찬영") # 이름
nums.append(12) # 12 추가
nums.append([10,20])
print(nums)
#2차원 리스트 ['김찬영', 12, [10, 20]] 0,1,2 번
#10만꺼낼거면 어케해야할까?
print(nums[2][0])
nums.insert(0, 20) #0번 자리에 20을 넣는단 소리 
print(nums)
nums.extend([10,20]) # 10과 20을 추가한다는 뜻
print(nums)
nums.extend("김찬영")
print(nums)
nums.extend(["김찬영"])
print(nums)

for s in scores:
    if s >= 75 :
        nums.append(s)
        print(nums)

nums.remove(20)
print(nums)

#삭제2 - pop()인덱스로 삭제 및 반환
last=nums.pop(2) #[10,20] #저장 후 삭제
print(last)
print(nums)
#삭제3
del nums[3]
print(nums)
#삭제4
""" nums.clear()
print(nums) """
#리스트 길이 확인
#위치 찾기(탐색) - index
print(len(nums)) #정수 - range(len*)
#개수(탐색) - count
print(nums.count(12))
#위치 찾기(탐색)-index
print(nums.index(12)) """

#순서 정렬 - sort()
nums = [30,10,20]
nums.sort()
print(nums)
nums.sort(reverse=True) #False오름차순/ True 내림차순
print(nums)
#뒤집기-revers()
nums.reverse() #뒤집기
print(nums)