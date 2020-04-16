from datetime import datetime
from bs4 import BeautifulSoup
import time
import requests
import SendMail
import call


# return a status of availability of a product
def status (url, headers):
    respond = requests.get(url, headers=headers)
    print('HTTP', respond.status_code)
    html = respond.content
    soup = BeautifulSoup(html, 'lxml')
    match = soup.find('div', class_='fulfillment-add-to-cart-button')
    status = match.text
    return status

# Start in 2 hours
#time.sleep(7200)
url0 = 'https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255' # Red switch
url1 = 'https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253'
url2 = 'https://www.bestbuy.com/site/nintendo-switch-animal-crossing-new-horizons-edition-32gb-console-multi/6401728.p?skuId=6401728'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
counter = 0
status_list = []  # Red, Black, Green color of switch

while True:
    counter += 1
    status_list = [status(url0, headers), status(url1, headers), status(url2, headers)]  #[Sold out, Sold out, Add to Cart] could be one of the examples
    time.sleep(1)
    print(datetime.now())
    body = "Red is {0}, Black is {1}, Green is {2}".format(status_list[0], status_list[1], status_list[2]) # Sold Out, Add to Cart, Check Stores
    print(body)

    print('Number of visit: {0}\n'.format(counter))

    if 'Add to Cart' in status_list:
        SendMail.sentmail()
        print("Calling you now....\n")
        call.call()

    time.sleep(13)
