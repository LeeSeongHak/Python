#if문
n = int(input('점수 : '))
if n >= 80 :
    print('合格です')
else :
    print('80점 미만입니다.')

a = 3
if 1 < a < 10 :
    print('yeah')

age = int(input())
if age < 19 :
    print('애들은 가라')
else:
    if age < 27 :
        print('대학생일듯')
    else :
        print('いらっしゃいませ')

#80점 미만은 불합격 출력
m = int(input('점수 : '))
if m >= 80 :
    print('合格です')
else :
    print('不合格です')

#점수에 따라 수우미양가 중 하나 출력 (2가지 방법중 1번 방법을 쓰는 쪽이 더 좋음.)
#1번째 방법
if 0 <= m <= 100 :
    if m >= 90 :
        print('수')
    elif m >= 80 :
        print('우')
    elif m >= 70 :
        print('미')
    elif m >= 60 :
        print('양')
    else :
        print('가')
else :
    print('입력오류')

#2번째 방법
if 0 <= m <= 100 :
    if m >= 90 :
        print('수')
    else :
        if m >= 80 :
            print('우')
        else :
            if m >= 70 :
                print('미')
            else :
                if m >= 60 :
                    print('양')
                else :
                    print('가')
else :
    print('입력 오류')

#연도를 입력받아 윤년, 평년 구분(4의 배수이면서 100의 배수는 아닌 해, 400의 배수인 해가 윤년)
year = int(input('연도를 입력해보시오'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print('윤년입니다')
else :
    print('평년입니다')

#예시
#입력할 진법(2/8/10/16) : 16
#입력값 : ff
#변환할 진법(2/8/10/16) : 2
#결과 : ff(16) -> 0b11111111(2)

try :
    a = int(input('입력할 진법(2/8/10/16) : '))
except ValueError :
    print('정수 숫자를 입력하셔야죠 ^^')

if a != 2 and a != 8 and a != 10 and a != 16 :
    print('다시 입력해주세요')
elif a == 2 :
    try :
        b = int(input("입력값 : "))
        if 0 <= b <= 1 :
            b2 = bin(b)
        else :
            print('2진법은 0과 1만 되요 ^^')
    except ValueError :
        print('제대로된 값을 입력하세요 ^^')
elif a == 8 :
    try :
        b = int(input("입력값 : "))
        if 0 <= b <= 7 :
            b2 = oct(b)
        else :
            print('8진법은 0부터 7까지 되요 ^^')
    except ValueError :
        print('제대로된 값을 입력하세요 ^^')
elif a == 10 :
    try :
        b = int(input("입력값 : "))
        b2 = str(b)
    except ValueError :
        print('제대로된 값을 입력하세요 ^^')
elif a == 16 :
    try :
        b = input("입력값 : ")
    except ValueError :
        print('제대로된 값을 입력하세요 ^^')
    b = int(b, 16)
    b2 = hex(b)
c = int(input('변환할 진법(2/8/10/16) : '))
if a == c :
    print('입력한 진법과 변환할 진법이 같습니다. 다시 입력해주세요')
elif c != 2 and c != 8 and c != 10 and c != 16 :
    print('다시 입력해주세요')
else :
    if c == 2 :
        d = bin(b)
    elif c == 8 :
        d = oct(b)
    elif c == 10 :
        d = str(b)
    else :
        d = hex(b)
    print('결과 :', b2, '(' + str(a) + ') -> ', d, '(' + str(c) + ')')
#결과 : ff(16) -> 0b11111111(2)
