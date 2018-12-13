class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_age(self):
       print('%s' % (self.__age))



hello = Student('vill', 15)
hello.print_age()
print(hello._Student__name)