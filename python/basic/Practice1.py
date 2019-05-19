##주민번호 받아서(모든예외처리하기) 나이, 성별 보여주기

import time
now = time.localtime()
#주민번호 resident registration number
rrn = None
#앞자리 front number
fn = 0
#뒷자리 back number
bn = 0
#나이
year = 0
#성별
gender = None
while True:
    rrn = input('주민번호를 입력하세요(형식:000000-0000000)')
    try:
        fn = int(rrn[0 : 6])
        bn = int(rrn[7 : 14])
    except ValueError :
        print('형식대로 숫자만 입력하세요')
        continue
    if len(rrn) != 14:
        print('길이. 제대로. 입력하세요')
        continue
    if rrn[6] != '-':
        print('-를 입력하세요')
        continue
    if int(rrn[2:4]) > 12:
        print('월은 12월까지입니다')
        continue
    if int(rrn[7]) != 1 and int(rrn[7]) != 2 and int(rrn[7]) != 3 and int(rrn[7]) != 4:
        print('성별확인불가. 제대로 입력해주세요')
        continue
    if int(rrn[7]) == 1 or int(rrn[7]) == 2:
        a = 100 - int(rrn[0:2])
        b = now.tm_year - 2000
        year = a + b
        if int(rrn[7]) == 1:
            gender = '남자'
        if int(rrn[7]) == 2:
            gender = '여자'
        break
    if int(rrn[7]) == 3 or int(rrn[7]) == 4:
        a = now.tm_year - 2000 + int(rrn[0:2])
        year = a
        if int(rrn[7]) == 3:
            gender = '남자'
        if int(rrn[7]) == 4:
            gender = '여자'
        break
print('나이는 %d세이고, 성별은 %s입니다.' % (year, gender))
