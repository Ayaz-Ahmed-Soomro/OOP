class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram



    def config(self):

        print(f"I have {self.cpu} and {self.ram} RAM")

#comp = Computer()
# this is the very First Method to call the Class Method
#Computer.config(comp)
# you can write this an other way
comp = Computer("Core i7", "16GB")
comp.config()
comp2 = Computer("Core i5", "8GB")
comp2.config()