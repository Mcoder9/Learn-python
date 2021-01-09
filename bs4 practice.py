import requests
import webbrowser
from bs4 import BeautifulSoup
address = 'https://coreyms.com/'
for page in range(2, 18):
    source = requests.get(address)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'lxml')
    # print(soup.prettify())
    for article in soup.find_all('article'):
        try:
            header = article.h2.a.text
            summary = article.find('div', class_='entry-content').p.text
            vid_src = article.find('iframe', class_='youtube-player')['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            yt_link = f'www.youtube.com/watch?v={vid_id}'

        except Exception:
            header = None
            summary = None
            yt_link = None

        print(header)
        print(summary)
        print(yt_link)
        print()
    address = f'https://coreyms.com/page/{page}'
