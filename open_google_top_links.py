import requests,webbrowser,bs4
google_url = 'https://pypi.org/search/?q='
print('Loading...')
# search = input()
search = 'python'
address = google_url+search
result = requests.get(address)
result.raise_for_status()
# result = open('check.html','r')
soup = bs4.BeautifulSoup(result.text,'lxml')
# print(soup.prettify())
anchor_class = soup.find_all('a', class_= 'package-snippet')
tab = 1
for links in anchor_class:
    link = links['href']
    #if tab<=5:
    webbrowser.open(link)
    #tab+=1
