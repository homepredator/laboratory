# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError
# from bs4 import BeautifulSoup

# try:
#     html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print('Сервер не найден!')
# else:
#     bs = BeautifulSoup(html.read(), 'html5lib') # html.parser, lxml, html5lib
#     print(bs.h1)

# print(html.read())
# print(bs.nonExistentTag)

# try:
#     badContent = bs.nonExistingTag.anotherTag
# except AttributeError as e:
#     print('Тэг не найден!')
# else:
#     if badContent == None:
#         print('Тэг не найден!')
#     else:
#         print(badContent)


# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError
# from bs4 import BeautifulSoup

# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     except URLError as e:
#         return None
#     try:
#         bs = BeautifulSoup(html.read(), 'lxml')
#         title = bs.body.h1
#     except AttributeError as e:
#         return None
#     return title

# title = getTitle('http://www.pythonscraping.com/pages/page1.html')
# if title == None:
#     print('Title could not be found!')
# else:
#     print(title)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

# bs = BeautifulSoup(html.read(), 'lxml') 

# nameList = bs.find_all('span', {'class':'green'})
# for name in nameList:
#     print(name.get_text())


# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'lxml') 

# nameList = bs.find(['h1'])
# for name in nameList:
#     print(name.get_text())


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

bs = BeautifulSoup(html.read(), 'lxml') 

nameList = bs.find('span', {'class':'green'}, 3)
for name in nameList:
    print(name.get_text())

nameCount = bs.find_all(text = 'Anna Pavlovna')
print(len(nameCount)) # количество слов словаре