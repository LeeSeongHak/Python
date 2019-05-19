#리스트 생성, 이중 리스트

li = [n*10 for n in range(1, 11)]
print(li)

li = []
for num in range(1,11,1):
    li.append(num)
print(li)

#리스트의 요소를 1~100중에서 3과 5의 배수로
li = [n for n in range(1,101) if n % 3 == 0 and n % 5 == 0]
print(li)

#다중배열 테스트
li= [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
print(li)
print(li[0])
print(li[0][0])

print(len(li))
print(len(li[0]))

print(type(li))
print(type(li[0]))
print(type(li[0][0]))

#위의 li 이용해서 1/2/3/4/5/6/7/8/9/10/ 출력
for sub in li:
    for item in sub:
        print(item, end='/')

# li[0][0] = 1
# li[0][1] = 2
for i in range(0, len(li)) :
    for j in range(len(li[i])) :
        # java의 printf와 같이 위치 지정하고 값을 넣어주는 형식.
        print('li[%d][%d] = %d' % (i, j, li[i][j]))



li= [[1,[[4,5],3]],2]
print(li[0][1][0][1])
