class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap= self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    class Laptop:

        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Shuvo' , 36)

s1.show()