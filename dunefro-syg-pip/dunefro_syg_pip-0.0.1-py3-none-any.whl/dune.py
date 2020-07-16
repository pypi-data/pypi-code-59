import os

class Dog:
    list_of_dogs = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_of_dogs.append((name,age))

    def show_dogs(self):
        return self.list_of_dogs

def main():
    a = Dog('german',10)
    b = Dog('pug',11)
    c = Dog('labrador', 5)
    print(a.show_dogs())
# main()