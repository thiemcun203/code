import pickle
# from shutil import copyfile
# copyfile('student_info.pkl', 'updated_info.pkl')
# with open('update_info.pkl','rb')as f:
with open('student_info.pkl','rb') as f:
    file=pickle.load(f)
# print(file)
file_copy=file.copy()
def add_student_info(new_student):
    for i,u in enumerate(file_copy):
        if u['id']==new_student['id']:
            file[i]=new_student
        else:
            continue
    with open('update_info.pkl','wb') as f:
            pickle.dump(file,f)
new_student = {
        'id': 20200000,
        'name': 'Nguyen Van Anh',
        'score': {
            'math': 7.8,
            'english': 8.4,
            'physics': 8.0,
        }
    }
add_student_info(new_student)