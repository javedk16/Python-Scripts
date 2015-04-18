import requests
from bs4 import BeautifulSoup
import sched
import time
import pynotify
import webbrowser

myproduct = 'macbook'
myprice = 35000
refresh_time = 10
url = 'http://www.olx.in/mumbai/q-' + myproduct

if __name__ == '__main__':
    while True:
       	time.sleep(refresh_time)
        r = requests.get(url)

        soup = BeautifulSoup(r.content)

        titles = soup.find_all('a',
                               {'class': 'marginright5 link linkWithHash detailsLink'
                               })
        rates = soup.find_all('strong', {'class': 'c000'})
        links = soup.find_all('a',
                              {'class': 'marginright5 link linkWithHash detailsLink'
                              })

        for (title, rate, link) in zip(titles, rates, links):
            product = title.text.strip().encode('ascii', 'ignore')
            price = rate.text.strip().encode('ascii', 'ignore')
            go_link = link.get('href')
            if myproduct in product and int(price) <= myprice:
                pynotify.init('Match Found!')
                n = pynotify.Notification(product, price)
                n.show()
                webbrowser.open(go_link, new=2)

