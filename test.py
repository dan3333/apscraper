from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/", username="dan", password="")
mydb = myclient["testdb"]
mycol = mydb["apartments"]

#mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)


profile = FirefoxProfile("/root/.mozilla/firefox/5l4f32wz.default")

driver = webdriver.Firefox(profile)
driver.get('https://www.facebook.com/groups/161162324086838/')

element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('globalContainer'))

print ("start")

soup = BeautifulSoup(driver.page_source, 'html.parser')

element = soup.find("h1", {"id": "seo_h1_tag"})
print (element.get_text())

elements = soup.find_all("div", class_="_5pcr userContentWrapper")

for el in elements:
    print ("\nApartment:\n---------")
    for text in el.find_all("h5"):
        print ("Name: "+text.get_text())
        name = text.get_text()
    for text in el.find_all("p"):
        print (text.get_text())
        desc = text.get_text()
    mydict = {"name": name, "description": desc}
    x = mycol.insert_one(mydict)




