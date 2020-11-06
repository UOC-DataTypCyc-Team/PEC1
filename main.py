from webscraping import WebScrapper

#Parameters
#URL = 'https://www.tuaceitedemotor.com/aceite-5w30-long-life-longlife-c102x2453154'
URL2 = 'https://www.tuaceitedemotor.com/'
NUM_LINKS = 20

if __name__ == "__main__":
    webscrapper = WebScrapper(url=URL2, num_links=NUM_LINKS)
    webscrapper.print_dataframe()
    #webscrapper.export_csv()