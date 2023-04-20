class Im:
    def __init__(self):
        print("Im!")
class Im_Cat(Im):
    def __init__(self):
        super().__init__()
        print("Cat!")
Im_Cat = Im_Cat()       
class Class1:
    var = 100
    def __init__(self):
        self.var = 45
class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)
Im_Cat = Class2()        
