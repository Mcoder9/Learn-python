import requests, bs4, os
os.chdir('C:\\Users\\Mgcoder\\Desktop\\xkcd')

url = 'https://xkcd.com'
for page in range(2408, 0, -1):
    source = requests.get(url)
    soup = bs4.BeautifulSoup(source.text, 'lxml')
    # print(soup.prettify())
    img_link = soup.find('div', id='comic').img['src']
    img_link = 'https:' + img_link
    print(img_link)
    img_content = requests.get(img_link).content
    # print(type(img_content))
    img_name = f'{page}.png'
    save_img = open(img_name, 'wb')
    save_img.write(img_content)
    save_img.close()
    url = 'https://xkcd.com/' + str(page)
