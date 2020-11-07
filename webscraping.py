from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


class WebScrapper():
    def __init__(self, url, num_links):
        """
        The constructor for the WebScrapper class.

        Attributes:
        oil_name_list (lst): A list of oil product names.
        oil_brand_list (lst): A list of oil product brands.
        oil_quantity_list (lst): A list of oil quantities.
        oil_price_list (lst): A list of oil product prices.
        links (lst): A list of links retrieved from the initial url.

        Args:
            url (str): A URL (Protocol + Hostname + Document to retrieve).
            num_links (int): Number of different links we want to retrieve starting from the url.
        """
        self.url = url
        self.num_links = num_links
        self.oil_name_list = []
        self.oil_brand_list = []
        self.oil_quantity_list = []
        self.oil_price_list = []
        self.links = []
        self.link2product_list = []


    def get_request(self, url=None):
        """
        The function to make a GET request to the web server.

        Args:
        url (str): A url is "None" unless a url is provided

        Returns:
            soup (obj): A clean tree-like object containing the fields and data of the original html document.
        """
        url = self.url if url is None else url
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        return soup


    # Coge todos los links de una web y los añade a la lista "links" del objeto (self.links)
    def get_links(self, url=None):
        """
        The function to get the hiperlinks from the starting url 

        Args:
        url (str): A url is "None" unless a url is provided

        Returns:
            None
        """
        soup = self.get_request(url)
        tags = soup('a')

        for tag in tags:
            try:
                if len(self.links) <= self.num_links:  
                    semilink = re.findall('^[^h\s].*',tag.get('href', None))
                    semilink = self.url + semilink[0]
                    link = re.findall('^http.*',tag.get('href', None))

                    if semilink and semilink not in self.links:
                        self.links.append(semilink)
                    elif link:
                        link = link[0]
                        if link not in self.links:
                            self.links.append(link)
                else:
                    break
                            
            except: 
                continue


    def net(self):
        """
        The function to get the hiperlinks from subsequent urls

        Returns:
            None
        """
        self.get_links()
        for link in self.links:
            if len(self.links) <= self.num_links:  
                self.get_links(link)
            else:
                break


    def parse(self):
        """
        The function to parse an html document.

        Returns:
            oil_name_list (lst): A list containing the names of the different oil products.
            oil_brand_list (lst): A list containing the brands of the different oil products.
            oil_quantity_list (lst): A list containing the quantities of the different oil products.
            oil_price_list (lst): A list containing the prices of the different oil products.
        """
        self.net()
        for link in self.links:
            try:            
                soup = self.get_request(link)
                oil_list = soup.find_all('div', {'class': 'sectiondataarea'})

            except:
                continue
            
            for i in range(1, len(oil_list)):
                try:
                    inconsistencies = ['Líquido']
                    oil_name = oil_list[i].find('div', {'class': 'PBItemName'}).text.rstrip()
                    oil_brand = oil_name.split(' ')[0]
                    if oil_brand in inconsistencies:
                        continue
                    oil_quantity = float(oil_name.split(' ')[-1].replace('L',''))
                    oil_price = oil_list[i].find('span', {'class': 'PBSalesPrice'}).text
                    oil_price = float(oil_price.replace(' EUR','').replace(',','.'))

                    self.oil_name_list.append(oil_name)
                    self.oil_brand_list.append(oil_brand)
                    self.oil_quantity_list.append(oil_quantity)
                    self.oil_price_list.append(oil_price)
                    self.link2product_list.append(link)

                except:
                    continue

        return self.oil_name_list, self.oil_brand_list, self.oil_quantity_list, self.oil_price_list, self.link2product_list



    def lists_to_dataframe(self):
        """
        The function to create a dataframe with all the data retrieved from the hiperlinks.

        Returns:
            df (obj): A dataframe containing all the attributes (columns) and registers (rows) with the parsed data.
        """
        oil_name_list, oil_brand_list, oil_quantity_list, oil_price_list, link2product_list = self.parse()
        data_tuples = list(zip(oil_name_list, oil_brand_list, oil_quantity_list, oil_price_list, link2product_list))
        df = pd.DataFrame(data_tuples, columns=['Name','Brand', 'Quantity (Liters)', 'Price (€)', 'Found in link (url)'])

        return df


    def print_dataframe(self):
        """
        The function to print the dataframe.

        Returns:
            None
        """
        df = self.data_calculation()
        print('\nThe webcrawler has retrieved {} web-pages successfully!!!\n\n{} products have been parsed successfully!!!\n\n{}'\
            .format(len(self.links)-1,len(self.oil_name_list), df.head(len(self.oil_name_list))))


    def export_csv(self) -> object:
        """
        This function export dataframe to csv file

        Returns:
            None
        """
        self.data_calculation().to_csv('data.csv', index = False)


    def data_calculation(self):
        """
        This function creates a new attribute from the "Price (€)" and "Quantity (Liters)" attributes.

        Returns:
            df (obj): A dataframe with the new attribute "Price by Liter (€)".
        """
        # We add the new column just before the column with the link where we found the product
        df = self.lists_to_dataframe()
        idx = len(df.columns) - 1
        price_per_liter = df["Price (€)"] / df["Quantity (Liters)"]
        df.insert(loc=idx, column="Price by Liter (€)", value=price_per_liter)
        datetime = pd.to_datetime('today')
        df.insert(loc=idx, column="Datetime", value=datetime)

        return df


######################################   RUN   ######################################


if __name__ == "__main__":
    URL = 'https://www.tuaceitedemotor.com/'
    NUM_LINKS = 25

    webscrapper = WebScrapper(url=URL, num_links=NUM_LINKS)
    webscrapper.print_dataframe()
    webscrapper.export_csv()


