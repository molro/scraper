 necesario installar
# Beautifulsoup4 python3 -m pip install beautifulsoup4
# Selenium python3 -m pip install selenium

from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver = webdriver.Firefox()
url = "https://www.sears.com.mx/categoria/15466/televisiones/pagina=1"
driver.get(url)

html = driver.page_source
driver.close()
soup = BeautifulSoup(html, "html.parser")
total_elements = soup.find_all("div", {"class":"countResults"})[0].string
products_page1 = soup.find('div',{'class':'boxProductosCategory'}).find_all('article')

# Report
print("Cantidad de elementos: " + total_elements)
with open('Sears_page1.csv', 'w', newline='') as csvfile:
  productwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  productwriter.writerow(['Description','price','img_url'])
  for product in products_page1:
    productwriter.writerow([product.find('p', {'class':'h4'}).text, product.find('p', {'class':'precio1'}).text, product.find('img')['src']])
    # print(product.find('p', {'class':'h4'}).text)
    # print(product.find('p', {'class':'precio1'}).text)
    # print(product.find('img')['src'])
print(len(products_page1))
# soup.find_all("article", {"class":"cardProduct"})[0].find('p', {'class':'h4'}).text
# soup.find_all("article", {"class":"cardProduct"})[0].find('p', {'class':'precio1'}).text
# soup.find_all("article", {"class":"cardProduct"})[0].find('img')['src']
