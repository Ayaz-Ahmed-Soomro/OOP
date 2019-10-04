class A: # Super Class/ Parent Class
    # COnstructor
    def __init__(self):
        print("I am Init COnstrctor")
    def feature1(self):
        print("I am the feature 1")
    def feature2(self):
        print("I am the Feature 2")
 # if we inhert two class this is class single level Inheritance like B(A)

class B: # Subclass/ Child Class
    # this is B constructor  so i you define B will call this but i you also want to call A class Construtor
    # just right below super().__init__(self)
    def __init__(self):
        super().__init__()
        print("i am B init")

    def feature3(self):
        print("I am the feature 3")

# you can also call the method by using super()
class C(A, B):

    def __init__(self):
        super().feature1()
        print("i am Init of C")

# when we call class A constrctor will be called even if you call B class which is inhertance of A Constr will be called
#s1 = A()


c1 = C()

