# * 내용을 입력하세요. ( 종료는 새로운 행에서 엔터키)
# aaaa
# bbbb
# 1111

# * 저장하시겠습니까? (y/n) Y
# * 파일명 : a.txt
# 이미 존재하는 파일입니다. 다시 입력하세요.
# * 파일명 : b.txt
# b.txt 파일이 저장되었습니다.

import shutil
import os

while True:
    text = input('* 내용을 입력하세요')
    if text == '':
        break
    f = open('save.txt', 'wt')
    f.write(text)
f.close()

while True:
    saveCheck = input('* 저장하시겠습니까? (y/n) ')
    if saveCheck == 'y' or saveCheck == 'Y':
        while True:
            fileName = input('파일명 : ')
            if os.path.exists(fileName):
                print('이미 존재하는 파일입니다. 다시 입력하세요.')
                continue
            else:
                shutil.copy('save.txt', fileName)
                print(fileName, '파일이 저장 되었습니다.')
                os.remove('save.txt')
                break
        break
    elif saveCheck == 'n' or saveCheck== 'N':
        print('저장하지 않고 종료합니다.')
        break
    else:
        print('y 또는 n을 입력해주세요')
        continue
