class Example:
    first_example = 123
    second_example = 55

    def __init__(self,age,weight):
        self.age = age
        self.weight = weight

    def func(self):
        self.l = 43
        print(self.l)

    def sum(self):
        return self.first_example + self.second_example

    def step(self):
        return self.age ** self.weight

Example_object = Example(1,2)
print(Example_object.first_example)
print(Example_object.sum())
print(Example_object.step())
print(Example_object.first_example)
Example_object.func()



