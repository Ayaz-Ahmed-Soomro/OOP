class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # we will define or laptop class here for use
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 8
        def show(self):
            print(self.cpu, self.ram, self.brand)


s1 = Student("Ayaz", 13)
s2 = Student("Aijaz", 12)

s1.show()
s2.show()
lap1 = s1.lap
lap2 = s2.lap
print(lap1.ram)
print(lap2.brand)
lap3=s1.lap
print(lap3.ram)
lap4 =Student.Laptop()
print(lap4.cpu)


# now see the magic of show method
# s8 is the object of Student class so it will print only name and roll no
s8 = Student("Sarfraz", 123)
s8.show()
# now it turn to laptop method show
# create a object for laptop class which is inner of student
s9 = Student.Laptop()
# you will see the i7 8 and hp 
s9.show()