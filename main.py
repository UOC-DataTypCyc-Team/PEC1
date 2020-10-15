from webscraping import WebScrapper

#Parameters
URL = 'https://www.tuaceitedemotor.com/aceite-5w30-long-life-longlife-c102x2453154'

if __name__ == "__main__":
    webscrapper = WebScrapper(url=URL)
    webscrapper.print_dataframe()
