# with open("file1.csv","w",encoding="UTF-8") as f:
#     f.writerow("Thiem,12,45,5")
import csv
with open('/Applications/Python 3.10/code/practise3/file1.csv') as file:
    reader = csv.reader(file,delimiter='\t')
    for row in reader:
        print(row)
csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]
with open('protagonist.csv', 'w') as file:
    writer = csv.writer(file).writerows(csv_rowlist)
    