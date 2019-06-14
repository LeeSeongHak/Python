#키보드로부터 정수를 입력받아 중복되지 않은 정수 5개의 리스트 생성
#검색할 정수 입력받음 -> 몇번째에 있는지 결과 출력(index()함수 사용)

nlist = []
cnt = 0

while cnt < 5 :
    try:
        n = int(input('정수 입력:'))
        if n in nlist :
            raise ValueError
        nlist.append(n)
        cnt += 1
    except:
        print('다시 입력해주세요.')

#검색할 정수 입력받음. 정수 아니면 다시 입력
while True:
    try:
        num = int(input('검색할 정수 입력:'))
        break
    except:
        print('다시 입력하세요.')
#검색할 정수가 리스트의 몇번째에 있는지 출력. 또는 없습니다.
try:
    idx = nlist.index(n)
    print('%d -> [%d]번 요소입니다.' % (n, idx))
except:
