###모듈 = 파이썬 코드를 작성해 놓은 스크립트 파일. 이 안에 함수, 변수, 클래스 등이 정의되어 있음.

import math as m

print(m.sqrt(2))

##math 모듈
#pi : 원주율 상수, tau : 원주율의 2배, e : 자연 대수 상수, inf : 무한대 값, nan : 숫자가 아닌 값을 의미
#sqrt(x) : x의 제곱근, pow(x,y) : x의 y승, hypot(x,y) x제곱 + y제곱의 제곱근 ...
import math

print(math.sin(math.radians(45)))
print(math.sqrt(2))
print(math.factorial(5))

import turtle as t
t.penup()
t.goto(-720,0)
t.pendown()
for x in range(-720, 720);
    t.goto(x,math.sin(math.radians(x)) * 100)
t.done()

##시간 - C언어와 달리 모든 값이 1부터 시작하기 때문에 따로 수정이 필요 X.
import time
print(time.time()       #값 : 현재시간을 에폭(Epoch) 시간(유닉스 시간)으로 표현.

#현재시간 보기 쉽게 바꾸기
t = time.time()
print(time.ctime(t))
print(time.localtime(t))

now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))

#1부터 999까지 출력하고 걸리는 시간 정하기
start = time.time()
for a in range(1000):
    print(a)
end = time.time()
print(end - start)

#실행 결과 정한 시간만큼 지연해서 뜨도록 하기
print('안녕하세요')
time.sleep(1)
print('밤에 성시경이 두 명 있으면 뭘까요?')
time.sleep(5)
print('야간투시경')

##달력
import calendar

print(calendar.calendar(2018))
print(calendar.month(2019, 1))
calendar.prcal(2018)

#첫 시작 요일 바꾸기(0~6). 0이 월요일. default값 월요일.
calendar.setfirstweekday(6)

##난수
import random

#5개의 난수 뽑기
for i in range(5):
    print(random.random())

#begin값과 end값 정해주기.
#randint(begin, end). randint(a, b)는 randrange(a, b + 1)와 같음. 즉, end값도 포함하여 난수 생성.
for i in range(5):
    print(random.randint(1, 10))

#해당 범위의 실수 난수 생성
for i in range(5):
    print(random.uniform(1,100))

#임의의 요소 하나를 골라 리턴하기
food = ["자장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))

#요소를 무작위로 섞기
random.shuffle(food)
print(food)

#랜덤으로 2개 뽑기
print(random.sample(food, 2))

#로또 번호 뽑기
nums = random.sample(range(1, 46), 6)
nums.sort()
print(nums)

#숫자 맞추기 게임
import random as r

secret = r.randint(1, 100)
count = 0
while True:
    num = int(input('숫자를 입력하세요(끝낼 때 0) : '))
    if num == 0:
        break
    count += 1
    if num == secret:
        print('%d번만에 맞췄습니다' % count)
        break
    elif num > secret:
        print('입력한 숫자보다 더 작습니다')
    else:
        print('입력한 숫자보다 더 큽니다')
