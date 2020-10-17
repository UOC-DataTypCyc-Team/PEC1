from bs4 import BeautifulSoup as soup
import requests
import pandas as pd


class WebScrapper():
    def __init__(self, url):
        """
        The constructor for the WebScrapper class.

        Attributes:
        oil_name_list (lst): A list of oil product names.
        oil_price_list (lst): A list of oil product prices.

        Parameters:
            url (str): A URL (Protocol + Hostname + Document to retrieve).
        """

        self.url = url
        self.oil_name_list = []
        self.oil_brand_list=[]
        self.oil_quantity_list=[]
        self.oil_price_list = []


    def get_request(self):
        """
        The function to make a GET request to the web server.

        Returns:
            page (obj): An object containing the html document.
        """

        req = requests.get(self.url)
        page = soup(req.text, 'html.parser')
        return page


    def parse(self):
        """
        The function to parse an html document.

        Returns:
            oil_name_list (lst): A list containing the names of the different oil products.
            oil_price_list (lst): A list containing the prices of the different oil products.
        """

        page = self.get_request()
        oil_list = page.find_all('div', {'class': 'sectiondataarea'})

        for i in range(1, len(oil_list)):

            oil_name = oil_list[i].find('div', {'class': 'PBItemName'}).text.rstrip()

            oil_brand = oil_name.split(' ')[0]

            oil_quantity = oil_name.split(' ')[-1].replace('L','')

            oil_price = oil_list[i].find('span', {'class': 'PBSalesPrice'}).text
            oil_price = float(oil_price.replace(' EUR','').replace(',','.'))

            self.oil_name_list.append(oil_name)
            self.oil_brand_list.append(oil_brand)
            self.oil_quantity_list.append(oil_quantity)
            self.oil_price_list.append(oil_price)

        return self.oil_name_list, self.oil_brand_list, self.oil_quantity_list, self.oil_price_list


    def lists_to_dataframe(self):
        """
        The function to print the dataframe.

        Returns:
            df (obj): A dataframe containing all the parsed data.
        """

        oil_name_list, oil_brand_list, oil_quantity_list, oil_price_list = self.parse()
        data_tuples = list(zip(oil_name_list, oil_brand_list, oil_quantity_list, oil_price_list))
        df = pd.DataFrame(data_tuples, columns=['Name','Brand', 'Quantity Liters', 'Price'])
        return df


    def print_dataframe(self):
        """
        The function to print the dataframe.

        Returns:
            None
        """

        df = self.lists_to_dataframe()
        print(df)
        #df.head(n=5)

    def export_csv(self) -> object:
        """
        This function export dataframe to csv file

        Returns:
            file(obj): A file csv with the data of dataframe(df)
        """

        self.lists_to_dataframe().to_csv('data.csv', index = False)

######################################   RUN   ######################################


if __name__ == "__main__":
    URL = 'https://www.tuaceitedemotor.com/aceite-5w30-long-life-longlife-c102x2453154'

    webscrapper = WebScrapper(url=URL)
    webscrapper.print_dataframe()
    #webscrapper.export_csv()
