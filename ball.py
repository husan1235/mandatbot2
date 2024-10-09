import requests
from bs4 import BeautifulSoup


async def get_ball(ID):
    url = f"https://mandat.dtm.uz/Home2022/AfterFilter?name={ID}&region=0&university=0"
    rawdata = requests.get(url)
    html = rawdata.content
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find_all('td')
    array = []
    for t in tr:
        text = t.text
        array.append(text)
    return array
