import requests
from bs4 import BeautifulSoup

site = "https://abt.uz"

def langs(url):
    lis = []
    link = []
    types = []
    get = requests.get(url)
    soup = BeautifulSoup(get.content, 'html.parser')
    a = soup.find("div", class_="col col-md-12 text-right sp-filter")
    b = str(a).split('<div class="ib">')
    soup2 = BeautifulSoup(b[2], 'html.parser')
    soup3 = BeautifulSoup(b[3], 'html.parser')
    y = soup2.find_all('a')
    z = soup3.find_all('a')
    for w in z:
        types.append(w.text)
    for x in y:
        lis.append(x.text)
        link.append(str(x['href']).split('&lang=')[1])
    return lis, link, types

def INFOY(url, name):
    print(url)
    lis1, Yname, kvota, kontr, grant = [], "", "", "", ""
    get = requests.get(url)
    soup = BeautifulSoup(get.content, 'html.parser')
    mydivs = soup.find("table", {"class": "table table-striped table-hover table-bold"})
    b = mydivs.find("tbody")
    for td in b.findAll('td'):
       lis1.append(td.text)
    for x, y, k, g in zip(range(0, len(lis1), 5), range(2, len(lis1), 5), range(3, len(lis1), 5), range(4, len(lis1), 5)):
        if lis1[x] in name:
            Yname += str(lis1[x])
            kvota += str(lis1[y])
            grant +=str(lis1[k])
            kontr +=str(lis1[g])
            
    get2 = requests.get(url)
    soup = BeautifulSoup(get2.content, 'html.parser')
    mydiv = soup.find("div", {"class": "col col-sm-4"})    
    imglink = mydiv.find("img", {"class": "img-responsive"}).get('src')

    return Yname, kvota, kontr, grant, imglink
