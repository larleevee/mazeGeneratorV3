

class Constants:

    def __init__(self):
        self.age = 18


class Test(Constants):

    def __init__(self):
        Constants.__init__(self)
        self.height = 180

    def get_age(self):
        return(self.age)

    def get_height(self):
        return(self.height)

Test = Test()
print(Test.get_age())
print(Test.get_height())

    
