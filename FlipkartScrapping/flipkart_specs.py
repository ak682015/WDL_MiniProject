import requests
from bs4 import BeautifulSoup


def get_products():
    for j in range(2, 10):
        url = r"https://www.flipkart.com/search?q=mobile&marketplace=FLIPKART&otracker=start&as-show=on&as=off&page=" + str(j)

        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'lxml')

        div_tag = soup.findAll("div", {'class': '_1-2Iqu row'})
        for i in div_tag:
            div_tag_name_sec = i.find("div", {'class': 'col col-7-12'})
            div_tag_name_third = div_tag_name_sec.find("div", {'class': '_3wU53n'})
            name_text = div_tag_name_third.text
            div_tag_price_sec = i.find("div", {'class': 'col col-5-12 _2o7WAb'})
            div_tag_price_third = div_tag_price_sec.find("div", {'class': '_1vC4OE _2rQ-NK'})
            price_text = div_tag_price_third.text
            print(name_text, '---', price_text)


get_products()
"""

#bhgxx2 col-12-12

url = r"https://www.flipkart.com/search?q=mobile&marketplace=FLIPKART&otracker=start&as-show=on&as=off&page=2"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

body = soup.findAll('dic',{'class':'_3BTv9X'})

for data in body:
    print(data)
    
"""
