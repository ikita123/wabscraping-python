from bs4 import BeautifulSoup
import json
import requests
def pickle():
    list=[]
    url_1=("https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471")
    req=requests.get(url_1)
    soup=BeautifulSoup(req.text,"html.parser")
    div=soup.find("div",class_="_1gX7")
    div1=div.span.get_text()
    b=div1[1:5]
    a=int(b)
    c=a//32
    i=1
    number=1
    while i<=c:
        url_2="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(i)
        req1=requests.get(url_1)
        soup1=BeautifulSoup(req.text,"html.parser")
        pickel_name=soup.find_all("div",class_="UGUy")
        pickel_rate=soup.find_all("div",class_="_1kMS")
        pickel_link=soup.find_all("div",class_="_3WhJ")
        j=0
        while j<len(pickel_name):
            name=pickel_name[j].get_text()
            rate=pickel_rate[j].span.get_text()
            link=pickel_link[j].a["href"]
            pickel_url="https://paytmmall.com"+link
            dict={"position":number,"name":name,"price":rate,"url":pickel_url}
            list.append(dict.copy())
            number=number+1
            j=j+1
        i=i+1
    with open("acchar.json","w") as data:
        json.dump(list,data,indent=4)
    return list
pickle()



                
                        


