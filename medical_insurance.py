import csv
dict_list = []
with open("insurance.csv", newline= "") as insurance_data:
    insurance_dict = csv.DictReader(insurance_data) 
    for row in insurance_dict:
        dict_list.append(row)


print(dict_list)




