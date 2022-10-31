from Rectangle import Rectangle
class Square(Rectangle):
    def __init__(self,a):
        Rectangle.__init__(self,a,a)
        self.copy_height=self.width
        self.copy_width=self.height
    def set_width(self, new_side):
        self.width=new_side
        self.height=new_side
    def set_height(self,new_side):
        self.width=new_side
        self.height=new_side
    
    # def set_height(self,new_height):
    #     self.a=new_height
    # def set_width(self,new_width):
    #     self.a=new_width
    
with open('Rectangle.py','w') as f:
    f.write('Hello')

        
        
        
        
        