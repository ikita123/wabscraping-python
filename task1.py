from bs4 import BeautifulSoup
import requests
import json
def scrap():
    req=("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
    r=requests.get(req)
    soup=BeautifulSoup(r.text,"html.parser")
    div=soup.find_all("td",class_="titleColumn") 
    number=0
    list=[]
    i=0
    while i<len(div):
        number=number+1
        movie=i.a.get_text()
        year=i.span.get_text()[1:5]
        year_1=int(year)
        i=i+1
        url="https://www.imdb.com/"+i.a["href"]
        rating=soup.find("td",class_="ratingColumn").strong.get_text()
        rating_1=float(rating)
        dict={"position":number,"name":movie,"year":year_1,"rating":rating_1,"url":url}
        list.append(dict)
        i=i+1
        dict={"position":"","name":"","year":"","rating":"","url":""}
        with open ("movie.json","w") as data:
            json.dump(list,data,indent=4)
    return list
scrap()



    