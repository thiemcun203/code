class Student:
    def __init__(self,name=None,age=None):
        self._name=name
        self._age=age
    @property #access as attribute
    def name(self):
        return self._name
    @name.setter # access as an attribute and set new value
    def name(self,new_name):
        print(f'Khong the doi ten {self.name} thanh {new_name} ')

thiem = Student()

print(thiem._name)
# thiem.name = 'Tuan'
# print(thiem._name)
# class Student:
#     def __init__(self,name):
# 		self._name = name
# 	@property
# 	def name(self):
# 		return self._name
# 	@name.setter
# 	def name(self,newname):
# 		self._name = newname
def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()
    return new_function

@decorator 
def initial_function():
    print("Initial Functionality")

initial_function()
decorator(initial_function())#same above
class Student:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')

# print(_Student__schoolName)