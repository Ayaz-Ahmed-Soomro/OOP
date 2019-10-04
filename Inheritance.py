class Calc:
    def add(self, x, y):
        return x + y

    def multi(self, x, y):
        return x * y


class SciCal(Calc):
    def add(self, x, y):
        if x < 0 or y < 0:
            return 0
        else:
            return x + y


obj1 = Calc()


print(obj1.add(10, 20))

obj2 = SciCal()
print(obj2.add(0, 5))
print("Multiplication of two nos: ", obj2.multi(10, 20))

print("this is add method of Calc Class", obj1.add(-5, 6))
print("this is override add method of add class", obj2.add(-5, 6))
