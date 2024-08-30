import requests
from bs4 import BeautifulSoup
import json
import logging

URL = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_6_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_6_0_na_na_na&as-pos=6&as-type=TRENDING&suggestionId=mobiles&requestId=f26dfa14-f53e-4fa1-8ab9-4f9de5985c2b"
logging.basicConfig(filename='scraper.log',level=logging.INFO)

def scrape_data():
    data = []
    try : 
        for page in range(1,3):

            response = requests.get(f"(URL)&page={page}")

            response.rasise_for_status()
            soup = BeautifulSoup(response.text,'html,parser')
            products = soup.find_all('div',class_='product')
            for product in products:
                name = product.find('span', class_ = 'name').text.strip()
                price = product.find('span', class_ = 'price').text.strip()
                rating = product.find('span', class_ = 'rating').text.strip()

                data.append({
                    'name':name,
                    'price':price,
                    'rating':rating
                })
                logging.info(f"Scrapped page {page}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during requests to {URL} : {str(e)}")
    return data


def save_data(data,filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)
    logging.info(f"data saved ro {filename}")


if __name__ == "__main__":
    scraped_data = scrape_data()
    save_data(scraped_data)