#Web Scrapping Module
#Use for the extracting the data fastly and easy to use
#Many module can use with Beautiful Soup for extracting the data
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())


# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')

# driver = webdriver.Chrome(chrome_options=options)
# source =driver.get('https://analyticsindiamag.com/')
# source_code=driver.page_source

# soup = BeautifulSoup(source_code,'lxml')
# article_block =soup.find_all('div',class_='post-title')

# for titles in article_block:
# 	title =titles.find('span').get_text()
# print(title)
from bs4 import BeautifulSoup
import requests  
URL = "https://multimeet.online/"
r = requests.get(URL)  
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
#prettify basically gives the visual presentation of the code.
#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

quotes=[] # a list to store quotes

table = soup.find('div', attrs = {'id':'all_quotes'})

for row in table.findAll('div',
						attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
	quote = {}
	quote['theme'] = row.h5.text
	quote['url'] = row.a['href']
	quote['img'] = row.img['src']
	quote['lines'] = row.img['alt'].split(" #")[0]
	quote['author'] = row.img['alt'].split(" #")[1]
	quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['theme','url','img','lines','author'])
	w.writeheader()
	for quote in quotes:
		w.writerow(quote)
