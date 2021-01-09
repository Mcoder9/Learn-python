import requests
import bs4
def reload():
    source = requests.get('https://www.worldtimeserver.com/time-zones/pkt/')
    source.raise_for_status()
    soup = bs4.BeautifulSoup(source.text, 'lxml')
    time = soup.find('span', id='theTime').text
    date = soup.find('span', class_='font6').text
    print(time)
    print(date)
    reload()
reload()
