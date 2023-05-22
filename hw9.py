class Point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y

    def show(self):
        print(f'({self.__x}, {self.__y})')

    def set(self,x,y):
        self.__x=x
        self.__y=y

    def get(self):
        return (self.__x,self.__y)

class Rectangle:
    def __init__(self,lx=0,ly=0,rx=0,ry=0):
        self.__lt=Point(lx,ly)
        self.__rb=Point(rx,ry)

    def show(self):
        print(f'좌측 상단 꼭지점이 {self.__lt.get()}이고 우측 하단 꼭지점이 {self.__rb.get()}인 사각형입니다.')

    def getWidth(self):
        lx=self.__lt.get()[0]
        rx=self.__rb.get()[0]
        return rx-lx

    def getHeight(self):
        ly=self.__lt.get()[1]
        ry=self.__rb.get()[1]
        return ry-ly

    def getArea(self):
        result=self.getWidth()*self.getHeight()
        return result

    def getPerimeter(self):
        result=(self.getWidth()+self.getHeight())*2
        return result

# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
