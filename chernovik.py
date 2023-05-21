import random
position = random.randint(0,3)
rooms =['кухня','спальня','тронный зал','гостинная']

class Person:
    def __init__(self, name, surname, room) -> None:
        self.name = name
        self.surname = surname
        self.room = room
 
    def __del__(self):
        print(f'был изгнан {self.name} {self.surname},{self.room}')
    def __str__(self) -> str:
        return f'Работник {self.name} {self.surname} {self.room}'
 
    def __eq__(self, other: 'Person'):
        return  self.room == other.room

sergik = Person('Валерий', 'Князев','кухня'),
kiralochek = Person('Александр', 'Потапов','гостинная'),
valera = Person('Сергей', 'Даниелян','спальня'),
#оно не работает, я не понял
input()