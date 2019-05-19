##튜플 - 값의 집합이라는 면에서 리스트와 유사하지만 초기화한 후 편집할 수 없다는 점이 다르다.
#튜플을 정의할 때에는 리스트의 []와 달리, ()로 정의한다.
tu = 1, 2, 3, 4, 5
print(tu[3])        #가능
print(tu[1:4])      #가능
print(tu + (6, 7))  #가능
print(tu * 2)       #가능
tu[1] = 100         #불가능
del tu[1]           #불가능

#튜플 사용 이유
#1.내부구조가 단순하고 빠르다. -> 속도도 빠르다 메모리도 덜 쓴다.
#2.편집할 수 없기 때문에 안정적이다.


##사전(Dictionary)은 키와 값의 쌍을 저장하는 대용량의 자료구조. 변경이 가능하다.
#사전은 키의 중복을 허락하지 않기 때문에 연관된 정보를 저장할 때 무척 실용적이다.
dic = { 'boy':'소년', 'school':'학교', 'book':'책'}
print(dic)
print(dic['boy'])
print(dic.get('student'))
print(dic.get('student', '사전에 없는 단어입니다.'))

if 'student' in dic :
    print('사전에 없는 단어입니다.')
else :
    print('이 단어는 사전에 없습니다.')

#삽입, 수정, 삭제
dic['boy'] = '남자애'
dic['girl'] = '소녀'
del dic['book']
print(dic)

#요소 값 알아내기
print(dic.keys())
print(dic.values())
print(dic.items())

keylist = dic.keys()
for key in keylist :
    print(key)

#사전 -> 리스트 변환하기
keylist = list(dic.keys())

#2개의 사전 병합하기. 'book'이라는 키가 중복되므로 값이 대체되고 나머지는 뒤로 병합된다.
dic = { 'boy':'소년', 'school':'학교', 'book':'책'}
dic2 = { 'student':'학생', 'teacher':'선생님', 'book':'서적'}
dic.update(dic2)
print(dic)

#리스트 -> 사전 변환하기
li = [ ['boy', '소년'], ['school', '학교'], ['book', '책'] ]
dic = dict(li)
print(dic)

#팝송에서 등장하는 알파벳 갯수 세기
song = """The club isn’t the best place to find a lover
So the bar is where I go
Me and my friends at the table doing shots
drinking fast and then we talk slow
you come over and start up a conversation
with just me and trust me
I’ll give it a chance now
Take my hand stop, put van the man
on the jukebox and then we start to dance
And now I’m singing like"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1
#정렬없이 띄우기
print(alphabet)
#정렬방법 1
key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet[c]
    print(c, "=>", num)
#정렬방법 2
for code in range(ord('a'), ord('z') + 1):
    c = chr(code)
    num = alphabet.get(c, 0)
    print(c, "=>", num)
