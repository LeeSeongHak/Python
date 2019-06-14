#while문 연습

student = 1
while student <= 5 :
    print(student, "번 학생의 성적을 처리한다.")
    student += 1

#1 기본 반복문
n = 1
while n < 5 :
    print('반복할 내용')
    n += 1
print('-' * 10)

#2 while True에서 break로 빠져나오기
n = 1
while True :
    print('반복할 내용')
    n += 1
    if n > 5 :
        break
print('-' * 10)

#3 continue 사용 예. if continue조건으로 인해 print가 4번이 아닌 3번만 실행됨.
n = 1
while n < 5 :
    n += 1
    if n == 2 :
        continue
    print(n, sep=",")
print('-' * 10)
