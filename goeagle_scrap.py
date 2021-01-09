# import requests
# import bs4
# def reload_():
#     source = requests.get('https://goeagle.pk/home')
#     source.raise_for_status()
#     #source = open('check.html', 'r')
#     soup = bs4.BeautifulSoup(source.text, 'lxml')
#     # print(soup.prettify())
#     for article in soup.find_all('div', class_='td_module_1 td_module_wrap td-animation-stack'):
#         title = article.h3.a.text
#         print('Post title:', title)
#         category = article.find('a', class_='td-post-category').text
#         print('Post category:', category)
#         ps_date = article.find('time', class_='entry-date updated td-module-date')['datetime']
#         print('Post date:', ps_date)
#         post_link = article.find('a', class_='td-image-wrap')['href']
#         print('Post link:', post_link)
#         print() # line space

#     reload_()
# reload_()
