#1. 정수를 반복 입력받아 양의정수만 합계. 0 입력하면 반복종료하고 결과 출력.
#결과 :
#양의 정수 개수 = 5 합계 = 100 평균 = 20
cnt = 0
sum = 0
while True :
    try :
        num = int(input("양의 정수만 입력하쇼"))
    except ValueError :
        print('정수만 입력하세요 ^^')
    if num > 0 :
        cnt += 1
        sum += num
    elif num == 0 :
        break
    else :
        print('양의 정수만 입력하셔야죠 ^^!')
        continue
avg = int(sum / cnt)

print("결과 : ")
print("양의 정수 개수 = " + str(cnt), "합계 = " + str(sum), "평균 = " + str(avg))
print('-' * 15)

#2. 문자 1개와 정수 1개를 입력 받음.
#해당 문자부터 (입력받은 정수)개 만큼의 Unicode표 출력
a = input("문자를 1개 입력하십쇼")
try :
    b = int(input('정수를 1개 입력해보십쇼'))
except ValueError :
    print('정수를 입력하십시오!')
try :
    c = ord(a)
    d = a + '(' + str(c) + ')'
    cnt = 0;

    if b >= 0 :
        while True :
            cnt += 1
            if cnt == b :
                break
            c += 1
            d += ' ' + chr(c) + '(' + str(c) + ')'
    elif b < 0 :
        while True :
            cnt -= 1
            if cnt == b :
                break
            c -= 1
            d += ' ' + chr(c) + '(' + str(c) + ')'
    print(d)
except TypeError :
    print('유니코드에 있는 문자를 입력하셔야해요^^!')
