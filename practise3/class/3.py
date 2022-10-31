class Student():
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id
        self.grade=grade 
    def __str__(self):
        return f'''Name: {self.name}
ID: {self.id}
Grade: {self.grade}'''
    def __lt__(self, other):
        if self.grade < other.grade:
            return True
        else: return False
    def __eq__(self, other):
        if self.id==other.id:
            return True
        else: return False
    def GradeType(self):
        if self.grade >=3.6: return "Excellent"
        elif 3.2<=self.grade <3.6: return "Good"
        elif 2.5<= self.grade <3.2: return "Fair"
        else: return "Poor"            
        
            
        