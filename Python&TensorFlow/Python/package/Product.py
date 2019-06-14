#클래스 정의
class Product2:
    #생성자
    def __init__(self, code, name, price):          #self는 자바에서의 this
        self.code = code
        self.name = name
        self.price = price
    #매서드 정의
    def printProduct(self):                         #매개변수가 없더라도 self를 써줘야한다!!
        print('코드는 %s, 이름은 %s, 가격은 %s원' % (self.code, self.name, self.price))

#클래스 정의 끝

#함수 정의
def test():
    print('product 모듈의 test()함수 실행')
