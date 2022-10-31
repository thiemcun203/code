import json

dict={'thiem':12,'ddicj':34,"SSs":[12,34]}
json_data_string=json.dumps(dict,indent=2,sort_keys=True)
converted_json_data_string=json.loads(json_data_string)
print(json_data_string)

# with open("jsonfile1.json","w+") as jf:
#     json.dump(dict, jf)
    
    
# with open("jsonfile1.json","r+") as ab:
#     print(json.load(ab))
    

# print(type(json_data_string))
# print(type(converted_json_data_string))