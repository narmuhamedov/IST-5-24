import requests
from bs4 import BeautifulSoup as Bs

URL = "https://adam.kg/ru/"

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
    }

#make request

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#get data

def get_data(html):
    bs = Bs(html, features='html.parser')
    items = bs.find_all('div', class_='col-md-4 mb-4')
    rezka_list = []
    for item in items:
        title = item.find('h6', class_='card-title').get_text(strip=True)
        image = 'URL' + item.find('div', class_='card border-0 bg-light h-100').find('img').get('src')
        rezka_list.append({
            'title': title,
            'image':image
        })
    return rezka_list

#func parser
def parsing_rezka():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list2 = []
        for page in range(1,2):
            response = get_html('https://adam.kg/ru/news/', params={'page': page})
            rezka_list2.extend(get_data(response.text))
        return rezka_list2
    else:
        raise Exception('Ошибка парсинга')

#print(parsing_rezka())




