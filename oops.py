class Human:
    def __init__(self, name, age, height):
            self.name = name
            self.age = age
            self.height = height

    def eating(self, food): #a method
        return '{} is eating {}'.format(self.name, food)

    def hello(self):
        return '{} prints hello'.format(self.name)

ram = Human("Ram", 18, 6)
nilesh = Human("Nilesh", 19, 6.1)

print("Height of {} is {}".format(ram.name, ram.height))
print("Height of {} is {}".format(nilesh.name, nilesh.height))

print(nilesh.hello())
print(ram.eating("Dinner"))