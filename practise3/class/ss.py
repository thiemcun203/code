# class Coordinate(object): 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance(self, other):
#         x_diff_sq = (self.x-other.x)**2 
#         y_diff_sq = (self.y-other.y)**2 
#         return (x_diff_sq + y_diff_sq)**0.5
#     def __str__(self):
#         return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
#     def __add__(self, other):
#         return Coordinate(self.x + other.x, self.y + other.y)
# c1 = Coordinate(3, 4)
# c2 = Coordinate(2, 1)
# print(c1)
# print(c1+c2)
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # return self.name
    def __str__(self):
        return str(self.name)
    # pass
print(Dog.__init__(Dog, "fff", 3)) # call hàm __init__ -> return chỉ dùng đc khi các hàm khác ko đc call
print(Dog("DD",34))
print(Dog.)
class Sales:
    def __init__(self, id):
        id = [4,2,1]
        self.id = id
val = Sales([1,2,3])
print (val.id)