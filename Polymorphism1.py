class Pycharm:   # Duck checking Polymorphism
    def execute(self):
        print("Compiling")
        print("Runing")



class MyEditor:
    def execute(self):
        print("Spell Checking")
        print("Grammar Checking")
        print("Code analysis")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Pycharm()
ide2 =MyEditor()



lap1 = Laptop()
lap1.code(ide)

lap2 = Laptop()
lap2.code(ide2)