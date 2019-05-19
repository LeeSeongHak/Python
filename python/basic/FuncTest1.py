##함수의 사용

#함수 정의
def test1():
    print('test1() 실행')

#함수 호출
test1()
test1()

#인수가 있는 함수
a = 20
def test2(a):
    print('전달된 인수 : ', a)

test2(10)
print(a)

#리턴값이 있는 함수
def test3():
    return 99

n = test3()
print(n)

#인수 또는 리턴값이 여러 개인 함수
def test4(a, b, c):
    d = a + b + c
    e = ( a + b + c ) / 3
    return d, e
    #return할 때 []로 묶어서 리턴하면 list, ()로 묶거나 여러개의 값을 그냥 리턴하면 tuple.

n = test4(1,2,3)
print(n[0])            #n의 타입 = tuple

#파이썬에서의 pass명령은 C나 자바의 {}와 같이 빈 함수를 정의할 때 활용
def a():
    pass

#가변 인수 - 가변 인수는 이후의 모든 인수를 다 포함하기 때문에 인수 목록의 마지막에 와야 한다.
def intsum(*ints):
    #여기서 ints도 tuple.
    sum = 0
    for num in ints:
        sum += num
    return sum

print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))
print(intsum(8, 9, 6, 2, 9, 7, 5, 8))
