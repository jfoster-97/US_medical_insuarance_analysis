import csv
import statistics as stat


dict_list = []
with open("insurance.csv", newline= "") as insurance_data:
    insurance_dict = csv.DictReader(insurance_data) 
    for row in insurance_dict:
        dict_list.append(row)
#returns dictionary of csv where id starting at 0 is key and value is dictionary of patient
def general_dict():
    id_dict = {}
    for row in range(len(dict_list)):
        id_dict[row] = dict_list[row]

    return id_dict

dict_by_id = general_dict()
#print(dict_by_id)
def individual_parameter_list(dict_by_id, var, datatype =str):
    parameter_list = []
    for id in dict_by_id:
        parameter_list.append(datatype((dict_by_id[id][var])))
    return parameter_list


ages = individual_parameter_list(dict_by_id, "age", int)
sexs = individual_parameter_list(dict_by_id, "sex")
bmis = individual_parameter_list(dict_by_id, "age", float)
childrens = individual_parameter_list(dict_by_id, "children", int)
smokers = individual_parameter_list(dict_by_id, "smoker")
regions = individual_parameter_list(dict_by_id, "region")
charges = individual_parameter_list(dict_by_id, "charges", float)

age_mean = round(stat.mean(ages), 0 )
# children_mean = round(stat.mean(childrens), 0)
# bmi_mean = round(stat.mean(bmis), 1)
# charges_mean = round(stat.mean(charges), 2)
# print(children_mean)
# print(bmi_mean)
# print(charges_mean)



def produce_dict(dict_by_id, var_key):
    new_dict = {}
    for person in dict_by_id:
        new_key = dict_by_id[person][var_key]
        new_value = dict_by_id[person]
        if new_key not in new_dict.keys():
            new_dict[new_key] = [new_value]
        else:
            temp_list = new_dict[new_key]
            temp_list.append(new_value)
            new_dict[new_key] = temp_list
    return new_dict

dict_by_region = produce_dict(dict_by_id, "region")
dict_by_sex = produce_dict(dict_by_id, "sex")
dict_by_smoker = produce_dict(dict_by_id, "smoker")
dict_by_age = produce_dict(dict_by_id, "age")
#Smokers Analysis 
def percent_smoker():
    num_smokers = len(dict_by_smoker["yes"])
    num_non_smokers = len(dict_by_smoker["no"])
    percent_smokers = (num_smokers / (num_non_smokers + num_smokers)) * 100
    return round(percent_smokers, 1)

def smoker_charge():
    smokers = dict_by_smoker["yes"]
    non_smokers = dict_by_smoker["no"] 
    smoker_charges = []
    non_smoker_charges = []
    for patient in smokers:
        smoker_charges.append(float(patient["charges"]))
    for patient in non_smokers:
        non_smoker_charges.append(float(patient["charges"]))
    return round(stat.mean(smoker_charges), 2), round(stat.mean(non_smoker_charges), 2)

smokers_avg_charge, non_smoker_avg_charge = smoker_charge()
difference_in_smoker_charge = smokers_avg_charge - non_smoker_avg_charge

print(f"The average price of medical insurance is ${smokers_avg_charge} for a smoker and ${non_smoker_avg_charge} for a non-smoker. On average, a smoker will pay ${difference_in_smoker_charge} more than a non-smoker. {percent_smoker()}% of the patients smoke.")

def percent_smoker_by_region(region):
    region_smoker = 0
    region_charge = []
    region_non_smoker = 0
    for patient in dict_by_region[region]:
        if patient["smoker"] == "no":
            region_non_smoker += 1
            region_charge.append(float(patient["charges"]))
        else:
            region_smoker += 1
            region_charge.append(float(patient["charges"]))
    
    per_smoker = 100 * (region_smoker / (region_smoker + region_non_smoker))
    return round(per_smoker, 1), round(stat.mean(region_charge), 2)

    

# print(percent_smoker_by_region("northeast"))
# print(percent_smoker_by_region("northwest"))
# print(percent_smoker_by_region("southeast"))
# print(percent_smoker_by_region("southwest"))

#Region breakdown


num_people_ne = len(dict_by_region["northeast"])
num_people_nw = len(dict_by_region["northwest"])
num_people_se = len(dict_by_region["southeast"])
num_people_sw = len(dict_by_region["southwest"])

#print(num_people_ne, num_people_nw, num_people_se, num_people_sw)


#age and bmi

def avg_bmi_for_age():
    age_bmi_dict = {}
    age_list = list(dict_by_age.keys())
    
    for age in sorted(age_list):
        age_bmi_dict[int(age)] = []
    
    for age in dict_by_age:
        bmi_temp_list = []
        for patient in dict_by_age[age]:
            bmi_temp_list.append(float(patient["bmi"]))
        age_bmi_dict[int(age)] = round((stat.mean(bmi_temp_list)), 3)
        
    return age_bmi_dict


print(avg_bmi_for_age())