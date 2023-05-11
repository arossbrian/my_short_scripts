class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):



        print("My name is " + self.name)
r1 = Robot("Brian", "red", 40)
print(r1.introduce_self())


# r1.name = "Brian"
# r1.color = "red"
# r1.weight = 34
#
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40
#
# r1.introduce_self()
# r2.introduce_self()