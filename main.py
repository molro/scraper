from abc import abstractmethod 
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

def get_html (url):
    url_to_scrap = url
    driver = webdriver.Firefox()
    driver.get(url_to_scrap)
    html = driver.page_source
    driver.close()
    return html 

def scraping(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    # get total elements of the category
    category_total = soup.find_all("div",{"class":"countResults"})[0].string
    print("Cantidad de elementos de la categoria: " + category_total)

    article_list = soup.find('div',{'class':'boxProductosCategory'}).find_all('article')
    return article_list

def to_csv(url):
    article_list = scraping(url)

    with open('Sears_page1.csv', 'w', newline='') as csvfile:
        article_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        article_writer.writerow(['description','price','img_url']) ## Refactorizar 
        for article in article_list:
            article_description = article.find('p', {'class':'h4'}).text
            article_price = article.find('p', {'class':'precio1'}).text
            article_img_url = article.find('img')['src']
            article_writer.writerow([article_description, article_price, article_img_url])
    
    print("Cantidad de elementos escritos en el csv: " + str(len(article_list)))

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
