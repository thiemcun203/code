import pickle
from shutil import copyfile
copyfile('student_info.pkl', 'updated_info.pkl')
# if already have overwrite , not append, or not have ID ->do nothing
# with open('updated_info.pkl','rb') as f:

def add_student_info(new_student):
    with open('updated_info.pkl','rb') as f:
        file=pickle.load(f)
    a=0
    if 'id'in new_student.keys():
        for i,u in enumerate(file):
            if new_student['id']==u['id']:
                file[i]=new_student
                a=1
                break
        if a==0:
            file.append(new_student)
    with open('updated_info.pkl','wb') as f1:
            pickle.dump(file,f1)



