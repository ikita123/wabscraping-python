import json
from tas2 import*
def scrape_movie_details (movie_url):
    url_name=input("enter the url name")
    for i in movie_url:
        if url_name==i["rank"]:
            link=str(i["url"])
            re=requests.get(link)
            soup=BeautifulSoup(re.text,"html.parser")
            div_1=soup.find_all("li",class_="meta-row clearfix")
            div_2=soup.find_all("div",class_="meta-label subtle")
            div_3=soup.find_all("div",class_="meta-value")
            dict_1={}
            i=0
            while i<len(div_1):
                k=div_2[i].get_text().strip()
                v=div_3[i].get_text().strip()
                list_=[]
                if k=="Director" or "Genre" or "Producer" or "Production Co" or "Original Language":
                    a=v.split()
                    list_.append(a)
                    dict_1.update({k:list_})
                else:
                    dict_1.update({k:v})
                i=i+1
            with open("v.json","w") as u:
                json.dump(dict_1,u,indent=4)
tas4_file=scrape_movie_details(tas2_file)  
pprint(tas4_file) 







       