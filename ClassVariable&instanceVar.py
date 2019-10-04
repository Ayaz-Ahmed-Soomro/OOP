class Car:
    # class variable
    #if you change this this will affect on  whole program..
    wheels = 4


    def __init__(self):
        # these are instance Variables
        self.mile = 10
        self.name = "BMW"



c1 = Car()
c2 = Car()
c1.mile = 9
# how to modify the class variable
# this modify the whole but if you want to modify some particular
Car.wheels = 5
##########################
c1.wheels = 4
print(c1.mile, c1.name, c1.wheels)
print(c2.mile, c2.name, c2.wheels)