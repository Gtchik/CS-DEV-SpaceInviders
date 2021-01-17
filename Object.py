from typing import TypeVar
Object = TypeVar("Object")

class Object:
        def __init__(self, type_:str=None, x:int=50, y:int=50, size:int=75, color:str='blue',score:int=0, life:int=1, description:str=''):
            self.__score = score
            self.__type=type_
            self.__x=x
            self.__y=y
            self.__size=size
            self.__color=color
            self.__draw=''
            self.__life=life
            self.__description=description


        def getDescription(self) -> int: 
            return self.__description
        def setDescription(self,description:int) -> Object:
            self.__description=description
            return self
        def getScore(self) -> int: 
            return self.__score
        def setScore(self,score:int) -> Object:
            self.__score=score
            return self
        def setType(self, type:str) -> Object:
            self.__type = type
            return self
        def getType(self) -> str:
            return self.__type
        def setLife(self, life:int) -> Object:
            self.__life = life
            return self
        def getLife(self) -> int:
            return self.__life
        def reduceLife(self) -> int:
            self.setLife(self.getLife()-1)
            return self.__life
        def addLife(self) -> int:
            self.setLife(self.getLife()+1)
            return self.__life
        def setDraw(self, draw:'Tkinter val') -> Object:
            self.__draw = draw
            return self
        def getDraw(self) -> 'Tkinter val':
            return self.__draw
        def setColor(self, color:str) -> Object:
            self.__color = color
            return self
        def getColor(self) -> str:
            return self.__color
        def setSize(self, size:int) -> Object:
            self.__size = size
            return self
        def getSize(self) -> int:
            return self.__size
        def setX(self, x:int) -> Object:
            self.__x = x
            return self
        def getX(self) -> int:
            return self.__x
        def setY(self, y:int) -> Object:
            self.__y = y
            return self
        def getY(self):
            return self.__y

        def getIdBox(self) -> tuple:
            return (self.getX(), self.getY(), self.getX()+self.getSize(), self.getY()+self.getSize())

        def move(self, dx:int, dy:int) -> Object:
            self.setX(self.getX()+dx)
            self.setY(self.getY()+dy)
            return self
