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
        oil_price_list (lst): A list of oil product prices.

        Parameters:
            url (str): A URL (Protocol + Hostname + Document to retrieve).
        """

        self.url = url
        self.oil_name_list = []
        self.oil_brand_list=[]
        self.oil_quantity_list=[]
        self.oil_price_list = []
        self.links= []
        self.num_links = num_links


    def get_request(self, url=None):
        """
        The function to make a GET request to the web server.

        Returns:
            page (obj): An object containing the html document.
        """
        url = self.url if url is None else url
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        return soup


    # Coge todos los links de una web y los añade a la lista "links" del objeto (self.links)
    def get_links(self, url=None):
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
                        #print(semilink)
                    elif link:
                        link = link[0]
                        if link not in self.links:
                            self.links.append(link)
                            #print(link)
                else:
                    break
                            
            except: 
                continue


    # Limitamos el tamaño de la red a unos cuantos enlaces llamando a "get_links" hasta llegar al tamaño que queremos
    def net(self):

        self.get_links()
        for link in self.links:
            if len(self.links) <= self.num_links:  
                self.get_links(link)
            else:
                print('\nThe webcrawler has retrieved {} web-pages successfully!!!'.format(len(self.links)))
                break


    def parse(self):
        """
        The function to parse an html document.

        Returns:
            oil_name_list (lst): A list containing the names of the different oil products.
            oil_price_list (lst): A list containing the prices of the different oil products.
        """

        # Llamamos a self.net para parsear el primer enlace
        self.net()

        # Del listado de enlaces que hemos conseguido, llamamos a get_request para parsear todos ellos y crear la base de datos
        for link in self.links:
            try:            
                soup = self.get_request(link)
                oil_list = soup.find_all('div', {'class': 'sectiondataarea'})

            except:
                continue
            
            for i in range(1, len(oil_list)):
                try:
                    oil_name = oil_list[i].find('div', {'class': 'PBItemName'}).text.rstrip()
                    oil_brand = oil_name.split(' ')[0]
                    oil_quantity = oil_name.split(' ')[-1].replace('L','')
                    oil_price = oil_list[i].find('span', {'class': 'PBSalesPrice'}).text
                    oil_price = float(oil_price.replace(' EUR','').replace(',','.'))

                    self.oil_name_list.append(oil_name)
                    self.oil_brand_list.append(oil_brand)
                    self.oil_quantity_list.append(oil_quantity)
                    self.oil_price_list.append(oil_price)

                except:
                    continue

        print('\n{} products have been parsed successfully!!!'.format(len(self.oil_name_list)))

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
        print('\n\n',df.head(100))
        #df.head()


    def export_csv(self) -> object:
        """
        This function export dataframe to csv file

        Returns:
            file(obj): A file csv with the data of dataframe(df)
        """

        self.lists_to_dataframe().to_csv('data.csv', index = False)


######################################   RUN   ######################################


if __name__ == "__main__":
    #URL = 'https://www.tuaceitedemotor.com/aceite-5w30-long-life-longlife-c102x2453154'
    URL2 = 'https://www.tuaceitedemotor.com/'
    NUM_LINKS = 20

    webscrapper = WebScrapper(url=URL2, num_links=NUM_LINKS)
    webscrapper.print_dataframe()


