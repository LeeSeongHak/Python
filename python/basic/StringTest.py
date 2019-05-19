##문자열 분리

s = input('문자열 입력해보시와요')

#첨자
print(s[2])             #문자열은 0부터 시작하므로 2일경우 3번째 문자를 보여줌
print(s[-2])            #뒤에서부터 찾을 때에는 맨 뒤의 글자가 -1. 이후 -2, -3, ...

#슬라이스
print(s[2:5])           #2 <= 문자열의 위치 < 5 이므로, 2,3,4번째 문자 출력
print(s[3:])            #3번 이상 문자열 전부 출력
print(s[:4])            #4번 미만 문자열 전부 출력
print(s[2:-2])          #앞에서부터 2에 위치하는 문자열부터 뒤에서부터 -2에 위치하는 문자열 앞까지 출력.

yoil = "월화수목금토일"
print(yoil[::2])        #앞에서부터 2칸씩 띄어 읽기
print(yoil[::-1])       #뒤에서부터 1칸씩 앞으로 오며 읽기

#검색
s = "python programming"
print(len(s))           #길이
print(s.find('o'))      #앞에서부터 o가 제일 처음 나오는 위치. 없으면 -1
print(s.rfind('o'))     #뒤에서부터 o가 제일 처음 나오는 위치. 없으면 -1
print(s.index('r'))     #find와 같으나 해당 문자 없을 때 예외 발생.
print(s.count('n'))     #특정 문자의 갯수를 세어 리턴. 없으면 0을 리턴.

#조사 - True or False로 답이 나옴
print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

name = '이성학'
if name.startswith('이'):
    print('이씨입니다.')
else:
    print('이씨가 아닙니다.')

file = 'girl.jpg'
if file.endswith('.jpg'):
    print('그림 파일입니다.')

#isalpha    -   모든 문자가 알파벳인지 조사한다.
#islower    -   모든 문자가 소문자인지 조사한다.
#isupper    -   모든 문자가 대문자인지 조사한다.
#isspace    -   모든 문자가 공백인지 조사한다.
#isalnum    -   모든 문자가 알파벳 또는 숫자인지 조사한다.
#isdecimal  -   모든 문자가 숫자인지 조사한다.(소수)
#isdigit    -   모든 문자가 숫자인지 조사한다.(0~9까지)
#isnumeric  -   모든 문자가 숫자인지 조사한다.
#isidentifier   -   명칭으로 쓸 수 있는 문자로만 구성되어 있는지 조사한다.
#isprintable    -   인쇄 가능한 문자로만 구성되어 있는지 조사한다.


#변경
s = 'hihi'
print(s.lower())
print(s.upper())
print(s)

print(s.swapcase())
print(s.capitalize())
print(s.title())

#앞뒤의 불필요한 공백 삭제
s = '  하하  '
print(s.lstrip())       #왼쪽 공백 삭제
print(s.rstrip())       #오른쪽 공백 삭제
print(s.strip())        #양쪽 공백 삭제

#분할
s = '가 나 다 라'
print(s.split())

s = '._.'
print(s.join('ㅇㅇㅇㅇ'))   #join메서드는 split과 반대로 각 문자 사이에 다른 문자열을 끼워 넣는 것.

#대체
s = '나는 배가 부르다.'
print(s.replace('부르다', '고프다'))

#정렬
s = '하하핫'
print(s.ljust(30))      #왼쪽 정렬
print(s.rjust(30))      #오른쪽 정렬
print(s.center(30))     #가운데 정렬

#포맷팅
#표식 및 설명 - %d : 정수, %f : 실수, %s : 문자열, %c : 문자 하나, %x : 16진수, %o : 8진수, %% : %문자
