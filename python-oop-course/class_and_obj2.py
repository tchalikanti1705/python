# lets create another class 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        #here we are using self to access the data fields of the class Person and print a greeting message.


person1 = Person("Teja", 25)
person1.greet()
# Output: Hello, my name is Teja and I am 25 years old.