# Exercise Questions Link: https://pynative.com/python-object-oriented-programming-oop-exercise/
# Online Compiler Link: https://pynative.com/online-python-code-editor-to-execute-python-code/

# Question 1: Create a Class with instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

carX = Vehicle(300, 20)
print("Question 1:", carX.max_speed, carX.mileage)


# Question 2: Create a Vehicle class without any variables and methods

class Vehicle2:
    pass

print("Question 2: Pass")


# Question 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle3:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
class bus(Vehicle3):
    pass


busX = bus("School Volvo", 180, 12)
print("Question 3 - Vehicle Name:", busX.name, "Speed:", busX.max_speed, "Mileage:", busX.mileage)


# Question 4: Class Inheritance

class Vehicle4:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus4(Vehicle4):
    def seating_capacity(self, capacity=50):
         return super().seating_capacity(capacity = 50)
    
BusY = Bus4("School Volvo", 180, 12)
print("Question 4:", BusY.seating_capacity(50)) 


# Question 5: Define a property that must have the same value for every class instance (object)

class Vehicle5:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus5(Vehicle5):
    pass

class Car5(Vehicle5):
    pass

busX = Bus5("School Volvo", 180, 12)
carX = Car5("Audi Q5", 240, 18)
print("Question 5:", busX.name, busX.color, busX.max_speed, busX.mileage)
print("           ", carX.name, carX.color, carX.max_speed, carX.mileage)


# Question 6: Class Inheritance
class Vehicle6:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    
class Bus6(Vehicle6):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

busX = Bus6("School Volvo", 180, 12, 31)
print("Question 6 - Total Amount of Bus Fare is:", busX.fare())


# Question 7: Check type of an object

class Vehicle7:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

class Bus7(Vehicle7):
    pass

BusX = Bus7("School Volvo", 180, 12, 31)
print("Question 7:", type(BusX))


# Question 8: Determine if a Python object is an instance of a class or its subclass

class Vehicle8:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    
class Bus8(Vehicle8):
    pass

BusX = Bus8("School Volvo", 180, 12, 31)

print("Question 8:", isinstance(BusX, Vehicle8))