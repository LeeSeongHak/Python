#텍스트 파일에 쓰기

#파일 열기
f = open('a.txt', 'wt')

#출력
f.write('aaaa\n')
f.write('가나다라\n')
f.write('1234\n')

#닫기
f.close()
