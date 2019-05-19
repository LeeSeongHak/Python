#텍스트 파일 읽기

#전체 읽기
try:
    f = open('a.txt', "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print('파일이 없습니다.')
finally:
    f.close()

#지정한 문자수 읽기
#read 함수는 한번에 읽을 수 있어 편리하지만 대용량의 파일을 읽을 때는 메모리를 많이 소모한다는 단점이 있다.
#아주 큰 파일을 읽을 때는 아래와 같이 잘라서(read(숫자)) 읽으면 된다.
f = open('a.txt', 'rt')
while True:
    text = f.read(10)
    if len(text) == 0: break        #문자수 체크해서 0일때 나가도록 하는 것.
    print(text, end = '')
f.close()

#1줄씩 읽기
f = open('a.txt', 'rt')
text = ''
line = 1
while True:
    row = f.readline()
    if not row: break                   #한 글자도 못읽었을 때 break 만나서 나가도록 하는 것.
    text += str(line) + " : " + row
    line += 1
f.close()
print(text)
