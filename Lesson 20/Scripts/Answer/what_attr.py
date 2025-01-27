class Test1:
    def __init__(self):
        self.x = 0

class Test2(Test1):
    x = 1
    def __init__(self, x):
        super().__init__()
        self.x = x


what_attr = Test2(2)
print(what_attr.x)
