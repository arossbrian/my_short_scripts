class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w

    def introduce_self(self):
        print("My name is " + self.name)
    
r1 = ("Brian", "red", 30)

print(r1.introduce_self())
