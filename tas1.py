from bs4 import BeautifulSoup
import requests
import json
import pprint
def scrap():
    url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    div=soup.find("table",class_="table")
    rank=div.find_all("td",class_="bold")
    rating=div.find_all("span",class_="tMeterScore")
    name=div.find_all("a",class_="unstyled articleLink")
    name=div.find_all("a",class_="unstyled articleLink")
    riviwe=div.find_all("td",class_="right hidden-xs")
    list1=[]
    dict1={"name":"","rating":"","rank":"","url":"","year":"","riviwe":""}
    for i in range(0,len(rank)):
        RANK=rank[i].get_text().strip()
        RATING=rating[i].get_text().strip()
        NAME=name[i].get_text().strip()
        RIVIWE=riviwe[i].get_text()
        a=NAME.split("(")
        b=a[-1][0:5-1]
        url_1=name[i]["href"].strip()
        url_2="https://www.rottentomatoes.com"+url_1
        dict1.update({"name":NAME,"rating":RATING,"rank":RANK,"url":url_2,"year":b,"riviwe":RIVIWE})
        list1.append(dict1.copy())
        with open ("m.json","w") as data:
            json.dump(list1,data,indent=4)
    return list1
tas1_file=scrap()
pprint(tas1_file)