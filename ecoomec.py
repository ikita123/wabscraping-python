from bs4 import BeautifulSoup
import json
import requests
url_2=("https://webscraper.io/test-sites")
url_3=requests.get(url_2)
soup=BeautifulSoup(url_3.text,"html.parser")
div=soup.find_all("h2",class_="site-heading")
list=[]
number=0
def ecommerce():
    for i in div:
        number+=1
        name=i.get_text().strip()
        url="https://webscraper.io/test-sites"+i.a["href"]
        dict={"position":number,"name":name,"url":url}
        list.append(dict)
        dict={"position":"","name":"","url":""}
        with open ("commerce.json","w") as data:
            json.dump(list,data,indent=4)
    return list
ecommerce()


