#the first closing bracket which is valid is always same with opening bracket
class string_utilities:
    # def __init__(self,s):
    #     pass
    # gán attributes value cho object so class_name(obj, a1_value, a2)
    # tạo attributes : self.a1=a1_value
    # khi không cần khai báo thuộc tính class(), ngược lại: class(para1, para2,...)
    # => dùng trong tạo object và có truyền giá trị vd bài này: string_utilities("{ƯƠ}").is_vailid_parenthese("{uo}")
    def is_valid_parenthese( self, s):
        bracket=[]
        for i in s:
            if i in ["{","[","("]:
                bracket.append(i)
            else:
                try: # nhỡ pop bị close>open empty list
                    close = bracket.pop()
                    if i =="}":
                        if close!="{" : return False
                    if i=="]":
                        if close!="[": return False
                    if i==")":
                        if close!="(": return False
                except: return False
        return True if bracket == [] else False
        #return not bracket 
# return này nếu vẫn dư ra (lẻ) thì false
    def reverse_words(self, s):
        lst=s.split()
        return " ".join(reversed(lst))

print(string_utilities.is_valid_parenthese(1223,'{{((){})}}'))