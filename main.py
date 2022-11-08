from abc import abstractmethod 
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

def to_drive (url):
    url_to_scrap = url
    driver = webdriver.Firefox()
    driver.get(url_to_scrap)
    html = driver.page_source
    driver.close()
    return html 

def scraping(url):
    html = to_drive(url)
    soup = BeautifulSoup(html, "html.parser")
    total_elements = soup.find_all("div",{"class":"countResults"})[0].string
    print("Cantidad de elementos: " + total_elements)
    products_page = soup.find('div',{'class':'boxProductosCategory'}).find_all('article')
    return products_page

def to_csv(url):
    products_page = scraping(url)

    with open('Sears_page1.csv', 'w', newline='') as csvfile:
        productwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        productwriter.writerow(['Description','price','img_url']) ## Refactorizar 
        for product in products_page:
            productwriter.writerow([product.find('p', {'class':'h4'}).text, product.find('p', {'class':'precio1'}).text, product.find('img')['src']])
    
    print(len(products_page))

if __name__ == "__main__":
    end=False
    while not end:
        print("***Scraper Menu***")
        print("Press 1 to scrap")
        print("Press 2 to exit")
        print("******************")
        option=input("Choose option:")
        try:
            option=int(option)
        except:
            option=0
        if (option<1 or option>2):
            print("Invalid option, try again")
        elif (option==1):
            to_csv("https://www.sears.com.mx/categoria/15466/televisiones/pagina=1")
        elif (option==2):
            print("Goodbye!")
            end=True
