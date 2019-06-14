#예외 처리
n = 0
try:
    n = 3 / 0
    print('n=', n)
except:
    print('예외발생')
else:
    print('예외 발생하지 않음')
finally:
    print('예외 상관없이 무조건 실행')
print('try구문과 상관없는 부분', n)

try:
    a = input('정수입력:')
    b = input('정수입력:')
    c = int(a) / int(b)
    print(a, '/', b, '=', c)
    print(d)
    li = [1,2,3]
    print(li[5])
    print('aaa'/'bbb')
except BaseException:
    print('가장 상위 exception 타입')
except ValueError:
    print('타입은 맞지만 값의 형식이 잘못됨')
except NameError:
    print('NameError발생')
except IndexError:
    print('IndexError발생')
except TypeError:
    print('TypeError발생')

while True:
    try:
        n = int(input('1~10까지의 정수를 입력하세요'))
        if n < 1 or n > 10 :
            raise ValueError        #고의적 예외 발생(JAVA에서 throw)
        if n % 2 == 0:
            print('짝수입니다.')
        break
    except:
        print('정수만 입력해주세요')
