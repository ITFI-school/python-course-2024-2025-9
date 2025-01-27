class One:
    z = 0

class Two:
    z = 1

class Test(Two, One):
    pass

print(Test.z)
