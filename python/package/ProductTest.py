import sys
sys.path.append("C:\\workspacePython\\package")          #모듈 경로 등록
                                                 #유닉스와 리눅스는 / , 윈도우는 \\
import Product       #같은 폴더 안에 있을 때 사용자가 만든 모듈 import가능
x = Product.Product2('A23', '사과', 111)        #모듈명.클래스명
x.printProduct()
Product.test()
