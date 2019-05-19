#기본 for 반복문 range(시작, 끝, 증가값)
for student in [1, 2, 3, 4, 5] :
    print(student, "번 학생의 성적을 처리한다.")

sum = 0
for num in range(2, 101, 2) :
    sum += num
print("sum =", sum)
#0 1 2 3 4 5 6 7 8 9
for num in range(0, 10) :
    print(num, end=' ')

#10 9 8 7 6 5 4 3 2 1
for num in range(10, 0, -1) :
    print(num, end=' ')

#1 3 5 7 9
for num in range(1, 10, 2) :
    print(num, end=' ')

#0 2 4 6 8
for num in range(0, 9, 2) :
    print(num, end=' ')

#10 20 30 40 50 60 70 80 90 100
for num in range(10, 101, 10) :
    print(num, end=' ')

#5 4 3 2 1
for num in range(5, 0, -1) :
    print(num, end=' ')

#1 10 100 1000 10000
a = 10
num = 1
num2 = 0
for cnt in range(1, 6) :
    num2 = ' ' + str(num)
    num *= a
    print(num2, end=' ')
