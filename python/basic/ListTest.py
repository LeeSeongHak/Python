#리스트 사용
nlist = [1, 2, 3, 4, 5]
print(nlist)
print(nlist[0])
print(len(nlist))

#3이 nlist안에 있는가를 물어보는 것
print(3 in nlist)

slist = ['aaaaa', 'bbbb', 'ccc']
print(slist)
print(slist[0])
print(len(slist))
print(len(slist[0]))
print('bbbb' in slist)
print('xx' not in slist[0])
print('aaaaa' is slist[0])
#흐음.......
print('[\'aaaaa\', \'bbbb\', \'ccc\']' is slist)
#2~4까지
sublist = nlist[2:4]
print(sublist)
#처음부터 4까지
print(nlist[:4])
#6에서 끝까지
print(nlist[6:])
#1~7까지 하나씩 건너뛰며
print(nlist[1:7:2])

#0번자리에 10 넣기
nlist[0] = 10
#0번이상 2번미만(0~1) 자리에 해당값 끼워넣기. 갯수 안맞아도 상관없이 다 들어감.
nlist[0:2] = [100, 200, 300, 400]
#맨 뒤에 500이라는 숫자 추가하기(배열크기 + 1)
nlist.append(500)
#배열의 0번째자리에 99라는 숫자 추가하기(배열크기 + 1). 기존 숫자 뒤로 밀림.
nlist.insert(0, 99)
#배열 뒤에 5, 6, 7 이라는 값 넣기(배열크기 + 3)
nlist = nlist + [5, 6, 7]
#배열 내의 같은 내용이 그대로 한번 더 들어감. ex)기존 배열값이 [1, 2, 3]일 경우 *2 하면 [1, 2, 3, 1, 2, 3]이 됨.
nlist = nlist * 2
#배열에서 0번째를 지우면 기존의 1번째가 0번째로 감. 지울 때 주의할 것.
del nlist[0]
#배열 범위만큼 지우기(rangeremove)
nlist[2:5] = []
#배열안에서 해당 값이 있는 위치 찾기. 여러개일 경우 맨 앞에 있는 것의 위치 알려줌.
print(nlist.index(4))
print(nlist.index(5))
#배열안에서 해당 값이 몇개나 있는지 세보기
print(nlist.count(5))
#배열안에서 가장 큰 숫자. 문자배열도 된다!싱기방기
print(max(mlist))
#배열안에서 가장 작은 숫자
print(min(slist))
#배열내의 값을 오름차 순으로 정렬하기
nlist.sort()
#배열내의 값을 내림차순으로 정렬하기
nlist.reverse()

print(nlist)
