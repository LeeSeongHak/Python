print('aaaa')

print('おはよう')

1+2

a = 1
if a == 1 :
    print('a는 1이다')
else :
    print('a는 1이 아니다')

for y in range(10) :
    for x in range(y) :
        print('*', end = '')
    print()

print('aaa', 'bbb', 'ccc', sep='\n', end='\n끝이예요')

print('aaa', 'bbb', 'ccc', sep='/', end='=>')

print('aaaa\nbbbbb')

num = int(input())

#키보드 입력
c= input('정수 입력 :')
print ('c = ', c)
#print(c + 1)
print(int(c) + 1)
print(c + "문자열")

d= input('실수 입력 :')
print ('d = ', d)
print(float(d) + 1)

e = int(input('정수 입력 :'))
print('e = ', e)

print(type(a))

g = 1
if type(g) == int :
    print('int타입입니다')
elif type(g) != int :
    print('int타입이 아닙니다')

h = '문자열'
if type(h) == str :
    print('문자열ㅇㅇ')
else :
    print('문자열 ㄴㄴ')

a = 1
a = 'aaaa'
print(type(a))

#del = 변수 삭제하기
del a

width = int(input('width :'))
height = int(input('height :'))
print('사각형의 면적 :', width * height)

#16진수 표기법. hex를 이용하면 입력한 그대로 print 가능
a = 0x2f
print(hex(a))

b = 1.23456
c = 1.5e10

#앞에 r을 붙이면 굳이 \를 2번 쓰지 않아도 자동으로 raw(날것)으로 인식해서 있는 그대로 써짐
print(r"c:\temp\new.txt")

#줄바꿈 하고 싶을 땐 """ or ''' 3개 쓰면 인식됨
s = """살어리 살어리랏다 청산에 살어리랏다 얄리얄리얄라셩 얄라리 얄라
        호호호"""
print(s)

#줄 끝에 \ 쓰면 줄바꿈 없이 끝까지 가는듯.
s1 = "강나무 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네 \
길은 외줄기 남도 삼백리 술 익는 마을마다 타는 저녁놀 \
구름에 달 가듯이 가는 나그네"
print(s1)

#코드값 출력하기
print(ord('K'))
print(chr(100))

#변수, 자료형

a = 0xf
b = 1.23456
c= 1.5e10

print(hex(a))

#input으로 받으면 무조건 str.
d = input()
#int()에서 , 뒤의 숫자는 진법을 의미. 2, 8, 10, 16 ... default = 10.
a = int(d, 16)

b = int(a)
print(a, b)

#round = 반올림 함수. 뒤의 숫자가 2일경우 소수점 2번째 자리까지 나타냄 뒤는 반올림.
#뒤의 숫자가 0일경우 소수점없애고 반올림. -2일경우 소수점 앞3번째 숫자까지 나타내고 뒤는 반올림.
b = 111234.56789
a = int(b)
a = round(b, -3)
print(a)

#진위형(class 'bool') - True, False, None. 앞글자 대문자 주의
a = 3
print(type(a)==int)

#연산자
a = 10
#Python에는 a++, ++a 가 없다. a += 1 로 해야함.
a += 1
print(a)

#고급 산술 연산자 - ** : 거듭제곱, // : 정수 나누기, % : 나머지
print(2 ** 10)

#문자열 연산
a = "aaa"
b = 'bbb'
c = a + b
d = a * 10
e = a + '1'
print(a, b, c, d , e)

#문자로 저장된 실수를 정수로 바꾸기
print(float('3.12313'))
print(10 + int(float("22.5")))

print(tuple(c))

#비트연산자
a = 3 # 0000 0011
print(a >> 1)   #시프트 연산자. 비트 오른쪽으로 1칸 밀기
print(a << 2)   #시프트 연산자. 비트 왼쪽으로 2칸 당기기
print(a & 5)    #둘다 1이어야 1
print(a | 5)    #둘 중 하나만 1이면 1
print(a ^ 1)    #둘이 같으면 0. 다르면 1
print(~a)       #1의 보수로 만들어줌. 0은 1로 1은 0으로. 비트 반전의 역할

#비교, 논리 비트연산자
a = 1
b = 2
print(a == b)
print(a > 0 and b > 0)
print(a > 0 or b > 0)
print(a >= 1 and a <= 10)
print(1 <= a <= 10) #Python에서는 이게 된다! すごいいい
print()
