class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
class CampusAddress(Address):
    def __init__(self,office):
        # Address.__init__(self,'Dai Co Viet', "01")
    
        self.office_number= office    
        self.street_name="Dai Co Viet"
        self.number="01"
obj = CampusAddress("B1")
print(obj.street_name, obj.number, obj.office_number)
print(isinstance(obj, Address), isinstance(obj, CampusAddress))