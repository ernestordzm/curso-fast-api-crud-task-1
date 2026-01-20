
class Animal:

    def __init__(self, kind) -> None:
        self.kind = kind

    def legs(self):
        pass

    def fly(self):
        pass

    def type(self):
        print(f'The type is {self.kind}')

class Dog(Animal):

    def legs(self):
        return 4
    
    def fly(self):
        return False
    
    def other(self):
        print('Todo')
    
class Bird(Animal):

    def legs(self):
        return 2
    
    def fly(self):
        return True
    

dog = Dog('Canine')
dog.type()
print (dog.kind)
print (dog.fly())


bird = Bird('bird')
print (bird.legs())