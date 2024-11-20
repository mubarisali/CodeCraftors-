import unittest
class Animals:
    def speak(self):
        return ""
    
class Dog(Animals):
    def speak(self):
        return  "woof!" 
    
class Cat(Animals):
    def speak(self):
        return  "meow!" 
    
if __name__ =="__main__":
    dog  = Dog()
    cat = Cat()
    print(dog.speak())
    print(cat.speak())