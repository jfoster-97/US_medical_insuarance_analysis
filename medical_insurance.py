import csv



dict_list = []
with open("insurance.csv", newline= "") as insurance_data:
    insurance_dict = csv.DictReader(insurance_data) 
    for row in insurance_dict:
        dict_list.append(row)




#new dictionary to append dictionary of each patient to a new id sarting at id = 0
id_dict = {}
for row in range(len(dict_list)):
    id_dict[str(row)] = dict_list[row]

#list of each idependant variable
new_id = []
ages = []
sexs = []
bmis = []
childrens = []
smokers = []
regions = []
charges = []
new_id = list(id_dict.keys())



for id in id_dict:
    new_id.append
    ages.append(int(id_dict[id]["age"]))
    sexs.append(id_dict[id]["sex"])
    bmis.append(float(id_dict[id]["bmi"]))
    childrens.append(int(id_dict[id]["children"]))
    smokers.append((id_dict[id]["smoker"]))
    regions.append(id_dict[id]["region"])
    charges.append(float(id_dict[id]["charges"]))

def dict_converter(new_id, ages, sexs, bmis, childrens, smokers, regions, charges):
    new_dict = {}
    for i in range(len(new_id)):
        new_dict[new_id[i]] = {"id": new_id[i],"age": ages[i], "sex": sexs[i], "bmi": bmis[i], "children": childrens[i], "smoker": smokers[i], "region": regions[i], "charges": charges[i]}
    return new_dict

id_dict2 = dict_converter(new_id, ages, sexs, bmis, childrens, smokers, regions, charges)
#print(id_dict2)
#general function to be used to calculate mean of float or integer lists
def calc_mean(value_list):
    total = 0
    for value in value_list:
        total += value
    mean = total / len(value_list)
    return mean
#means of categories
age_mean = round(calc_mean(ages), 0 )
children_mean = round(calc_mean(childrens), 0)
bmi_mean = round(calc_mean(bmis), 1)
charges_mean = round(calc_mean(charges), 2)
# print(age_mean)
# print(children_mean)
# print(bmi_mean)
# print(charges_mean)

northeast = []
for id in id_dict2:
    if id_dict2[id]["region"] == "northeast":
        northeast.append(id_dict2[id])





def produce_dict(id_dict2, var_key):
    new_dict = {}
    for person in id_dict2:
        new_key = id_dict2[person][var_key]
        new_value = id_dict2[person]
        if new_key not in new_dict.keys():
            new_dict[new_key] = [new_value]
        
        else:
            temp_list = new_dict[new_key]
            temp_list.append(new_value)
            new_dict[new_key] = temp_list
    return new_dict

region_dict = produce_dict(id_dict2, "region")
sex_dict = produce_dict(id_dict2, "sex")

#print(region_dict)
print(sex_dict["male"])

# region_dict = new_region_dict(id_dict)

# def empty_region_dict(id_dict2):
#     region_dict = {}
#     north_east = []
#     south_east = []
#     north_west = []
#     south_west = []
#     for id in id_dict2:
#         key = id_dict2[id]["region"]
#         if key not in region_dict.keys():
#              region_dict[key] = []
#     for id in id_dict2:
#         if id_dict2[id]["region"] == "northeast":
#             north_east.append(id_dict[id])
#         elif id_dict2[id]["region"] == "southeast":
#             south_east.append(id_dict[id])
#         elif id_dict2[id]["region"] == "northwest":
#             north_west.append(id_dict[id])
#         else:
#             south_west.append(id_dict[id])
#     region_dict["northeast"] = north_east
#     region_dict["northwest"] = north_west
#     region_dict["southeast"] = south_east
#     region_dict["southwest"] = south_west
#     return region_dict

# print(empty_region_dict(id_dict)["northeast"])

