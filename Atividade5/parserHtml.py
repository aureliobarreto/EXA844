import urllib.request
from bs4 import BeautifulSoup

with open('seeds.txt') as arq:
    linhas = arq.readlines()
for linha in linhas:
    page = urllib.request.urlopen(linha)
    html = str(page.read().decode('utf-8'))
    soup = BeautifulSoup(html, 'lxml')
    print("<h1>"+ soup.title.string + "</h1>")
    for img in soup.find_all('img'):
        if img.get('src').startswith("https://"):
            print("<img src=\"" + img.attrs.get("src")+"\" width=\"500\" height=\"300\">")
        else:
            linha = linha.replace('\n','')
            link = linha+img.get('src')
            print("<img src=\""+link+"\" width=\"500\" height=\"300\" >")
   
