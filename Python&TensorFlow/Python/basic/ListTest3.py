#정수 10개를 입력받아 리스트에 저장
#그 값들의 평균과 10이상 차이나는 정수들 출력
#[결과 예]
#입력한 정수 : [1,2,3,4,5,40,55,-31,-5,10]
#평균 : 8.4
#결과 : 40 55 -31 -5

li = []
sum = 0
avg = 0
for num in range(0, 10, 1):
    try :
        n = int(input('정수를 입력하세요'))
        sum += n
        li.append(n)
    except ValueError :
        print('정수를 입력하십시오!')

avg = sum / len(li)
print('입력한 정수 :', li)
print('평균 :', avg)

li2 = []
print('결과 : ', end='')
for num in range(0, len(li)):
    if li[num] - avg >= 10 or avg - li[num] >= 10 :
        li2 = li[num]
        print(li2, end=' ')
