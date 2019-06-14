#1부터 n까지의 합계
def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

print('~ 4 =', calcsum(4))

#1.전달된 정수 사이의 합계 리턴
def sum(n, m):
    sum = 0
    for n in range(m + 1):
        sum += n
    return sum
n = sum(1, 5)       #15
print(n)

#2.전달된 정수까지의 팩토리얼
def fact(n):
    f = 1
    for n in range(1, n + 1, 1):
        f *= n
    return f

n = fact(4)         #24
print(n)

#3.전달된 정수까지의 짝수의 합계
def sum2(n):
    sum = 0
    for n in range(1, n + 1, 1):
        if n % 2 == 0:
            sum += n
    return sum
n = sum2(10)        #30
print(n)

#4.정수를 5개 전달받아 합계와 평균 리턴
def totavg(*ints):
    print(ints)
    sum = 0
    avg = 0
    for num in ints:
        sum += num
    avg = sum / len(ints)
    return sum, avg
a = int(input('첫번째 정수 : '))
b = int(input('두번째 정수 : '))
c = int(input('세번째 정수 : '))
d = int(input('네번째 정수 : '))
e = int(input('다섯번째 정수 : '))
n = totavg(a,b,c,d,e)
print(n)
