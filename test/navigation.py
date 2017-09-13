from bs4 import BeautifulSoup

file = open("test.html","r")
html= file.read()
file.close()

soup = BeautifulSoup(html, 'html.parser')

print(soup.title,'\n',soup.title.name,'\n',soup.title.string,'\n',soup.title.parent.name)
