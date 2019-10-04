# there are three types of Methods
# 1. Instance Method
# 2. Class Method
# 3. Static Method



class Student:
    # Class Varaible
    school = "Umar Daho"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    # this is instance Method
    def show(self):
        print(self.m1, self.m2, self.m3)
    def avrg(self):
        return (self.m1 + self.m2 + self.m3) / 3
    # this is class method
    @classmethod
    def info(cls):
        print(cls.school)
    # if we want to define a function which don't have any relation with class and attribute we will define it static method
    @staticmethod
    def info_all():
        print("This was our Method types Module in which we study three types of method..")

s1 = Student("S1", "s2", "s3")
s2 = Student(10, 20, 30)
avg=s2.avrg()
print("The Average Marks S2 are: ", avg)
s2.show()

s1.show()
# how to access class method
Student.info()
s1.info()


Student.info_all()
s1.info_all()
