
from  tas1 import *
dict_1={}
def group_of_year(movies):
    list_1=[]
    for i in movies:
        if i["year"] not in list_1:
            list_1.append(i["year"])
    for j in list_1:
        list_2=[]
        for l in movies:
            if j==l["year"]:
                list_2.append(l)
            dict_1.update({j:list_2})
        with open("w.json","w") as u:
            json.dump(dict_1,u,indent=4)
    return dict_1
tas2_file=group_of_year(tas1_file)