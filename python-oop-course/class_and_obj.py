class Car:
    #init method is a special method in python that is called when an object of the class is created. 
    #It is used to initialize the data fields of the class.
    def __init__(self, carname, carmodel, caryear, carcolor, ownerobj):
        self.name = carname
        self.model = carmodel
        self.year = caryear
        self.color = carcolor  #these all are the data fields or instance variables of the class Car
        self.owner = ownerobj  #this is a data field that will hold the reference to the owner object of the car

#lets create a class owners for each car 
class Owner:
    def __init__(self, ownername, ownerage):
        self.name = ownername
        self.age = ownerage
#now we need to pass
owner1 = Owner("John Doe", 45)
car1 = Car("BMW", "X5", 2020, "Black", owner1) #owner1 is the object of the class Owner that we are passing as an argument to the constructor of the class Car to initialize the owner data field of the car1 object.
print(car1.name)  # Output: BMW 
#we can access the data fields of the class Car using the object car1 and the dot operator.
print(car1.model)  # Output: X5
print(car1.year)  # Output: 2020
print(car1.color)  # Output: Black

#now we can also access the data fields of the owner object that is associated with the car1 object using the dot operator.
print(car1.owner.name)  # Output: John Doe