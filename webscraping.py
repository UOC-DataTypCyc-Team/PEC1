from bs4 import BeautifulSoup as soup
import requests
import pandas as pd


def webscraping():
    url = 'https://www.tuaceitedemotor.com/aceite-5w30-long-life-longlife-c102x2453154'
    req = requests.get(url)

    page = soup(req.text, 'html.parser')
    oil_list = page.find_all('div', {'class': 'sectiondataarea'})


    oil_name_list = []
    oil_price_list = []

    for i in range(1, len(oil_list)):
        oil_name = oil_list[i].find('div', {'class': 'PBItemName'}).text
        oil_price = oil_list[i].find('span', {'class': 'PBSalesPrice'}).text
        oil_name_list.append(oil_name)
        oil_price_list.append(oil_price)

    data_tuples = list(zip(oil_name_list, oil_price_list))
    df = pd.DataFrame(data_tuples, columns=['Name', 'Price'])
    print(df)
