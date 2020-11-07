import argparse
from webscraping import WebScrapper


######################################   ASIGN VARIABLES   ######################################

URL = 'https://www.tuaceitedemotor.com/'
NUM_LINKS = 20

######################################   RUN   ######################################

if __name__ == "__main__":
    #The parameters can be introduced by the user
    parser = argparse.ArgumentParser(description='Pipeline execution')
    parser.add_argument('-u', '--url', default=URL, help='The user can provide a different url from the default one (https://www.tuaceitedemotor.com/)')
    parser.add_argument('-n', '--numlinks', type=int, default=NUM_LINKS, help='The number of links that the user wants to retrieve')
    args = parser.parse_args()


    webscrapper = WebScrapper(args.url, args.numlinks)
    webscrapper.print_dataframe()
    webscrapper.export_csv()