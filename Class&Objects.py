class Calc:

    def add(self, x, y):
        return x + y

class Computer:


    def config(self):
        print("i7 , 5gb and 1TB")



comp = Computer()
print(comp.config())

obj1 = Calc()
print(obj1.add(10, 6))
obj2 = Calc()
print(obj2.add(10, 30))
