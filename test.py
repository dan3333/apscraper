from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pymongo
import hashlib 

myclient = pymongo.MongoClient("mongodb://localhost:27017/", username="dan", password="temp_pass")
mydb = myclient["testdb"]
mycol = mydb["apartments"]

#mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)


profile = FirefoxProfile("/root/.mozilla/firefox/5l4f32wz.default")
#profile = FirefoxProfile("/home/danb/.mozilla/firefox/6ne2qskf.default")

driver = webdriver.Firefox(profile)
driver.get('https://www.facebook.com/groups/599822590152094/')

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
    hash_obj = hashlib.md5(desc.encode())
    print ("Hash: "+hash_obj.hexdigest())
    mydict = {"name": name, "description": desc}
    x = mycol.insert_one(mydict)




