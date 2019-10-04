class A: # Super Class/ Parent Class
    def feature1(self):
        print("I am the feature 1")
    def feature2(self):
        print("I am the Feature 2")
 # if we inhert two class this is class single level Inheritance like B(A)

class B(A): # Subclass/ Child Class
    def feature3(self):
        print("I am the feature 3")
# Multilevel Inheritance Appraoch
class C(B):
    def feature4(self):
        print("i am the feature 4")

class D:
    def feature5(self):
        print("i am feature 5")

# this is multiple Inheritance
class E(C, D):
    def feature6(self):
        print(" I am feature 6")
a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature2()
b1.feature1()
b1.feature3()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()


# now if you create a object of E you will be find D method also
e1 = E()
e1.feature5()