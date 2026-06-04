class User:
    def __init__(self):
        self.name = 'Nishtha'
    def login(self):
        print('login')

class Student(User):
    def enroll(self):
        print('enroll')

u = User()
s = Student()
print(s.name)
s.login()
s.enroll()
# Class diagram: inheritance me arrow symbol hota h towards parent class & aggregation me diamond symbol hota h owner class ke towards hota h