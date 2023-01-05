'''
•Navigation
•Checking title
•Typing text on a text box
•Clicking a button that returns updated results on the page
•Selecting an item from the returned results and taking action on it
'''

import os
import time
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import  Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_path = "D:\\PIATEK\\chromedriver.exe" #chrome driver path

profile_path = "C:\\Users\\salem\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\vesjuulb.selenium" #firefox profile path
options = Options()
options.set_preference('profile', profile_path)
service = Service("D:\\PIATEK\\geckodriver.exe") #firefox driver path


def test_chrome_ebay():
    driver = webdriver.Chrome(chrome_path)
    driver.implicitly_wait(10)
    driver.get("https://www.ebay.com")
    get_title = driver.title #getting title
    driver.find_element(By.LINK_TEXT, "Electronics").click() # navigate to the Electronics tab
    driver.find_element(By.ID, "gh-shop-a").click() #opening navigation menu - "shop by category"
    driver.find_element(By.LINK_TEXT, "Pet supplies").click() # > to pet supplies
    driver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) > .b-guidancecard__link .b-img").click() #to the dog supplies with image
    driver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) > .b-guidancecard__link .b-img").click() #to the dog toys with image

    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .seo-breadcrumb-text > span").click() #navigate to homepage, look img/home2.png

    driver.find_element(By.ID, "gh-ac").click() #click to search bar
    driver.find_element(By.ID, "gh-ac").send_keys("piatek milan kit") #search for the merch
    driver.find_element(By.ID, "gh-ac").send_keys(Keys.ENTER) #click enter
    
    #### mouse scroll ########
    driver.execute_script("window.scrollBy(0,250)")
    driver.execute_script("window.scrollBy(250,500)")
    driver.execute_script("window.scrollBy(500,750)")
    driver.execute_script("window.scrollBy(750,400)")
    driver.execute_script("window.scrollBy(400,0)")
    ### end of the mouse scroll ####

    piatekKit = "https://www.ebay.com/itm/143522730556?var=442479409978" 
    driver.get(piatekKit) #go for a piatek kit

    driver.find_element(By.ID, "gh-la").click() #navigate to homepage with ebay icon on left-top

    SonyLens = "https://www.ebay.com/itm/185643427582"
    driver.get(SonyLens) # go for a sony lens

    quantity = driver.find_element(By.ID,"qtyTextBox") #quantity bar for ebay
    quantity.click()
    quantity.clear() #clear quantity bar
    quantity.send_keys("2") # write 2 in quantity bar

    print("The title is:" , get_title) #print title


def test_firefox_ebay():
    fdriver = Firefox(service=service, options=options)
    fdriver.get("https://www.ebay.com")
    fdriver.implicitly_wait(10)
    get_title = fdriver.title #getting title
    fdriver.find_element(By.LINK_TEXT, "Electronics").click() # navigate to the Electronics tab
    fdriver.find_element(By.ID, "gh-shop-a").click() #opening navigation menu - "shop by category"
    fdriver.find_element(By.LINK_TEXT, "Pet supplies").click() # > to pet supplies
    fdriver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) > .b-guidancecard__link .b-img").click() #to the dog supplies with image
    fdriver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) > .b-guidancecard__link .b-img").click() #to the dog toys with image

    fdriver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .seo-breadcrumb-text > span").click() #navigate to homepage, look img/home2.png

    fdriver.find_element(By.ID, "gh-ac").click() #click to search bar
    fdriver.find_element(By.ID, "gh-ac").send_keys("piatek milan kit") #search for the merch
    fdriver.find_element(By.ID, "gh-ac").send_keys(Keys.ENTER) #click enter

    #### mouse scroll ########
    fdriver.execute_script("window.scrollBy(0,250)")
    fdriver.execute_script("window.scrollBy(250,500)")
    fdriver.execute_script("window.scrollBy(500,750)")
    fdriver.execute_script("window.scrollBy(750,400)")
    fdriver.execute_script("window.scrollBy(400,0)")
    ### end of the mouse scroll ####

    piatekKit = "https://www.ebay.com/itm/143522730556?var=442479409978" 
    fdriver.get(piatekKit) #go for a piatek kit

    fdriver.find_element(By.ID, "gh-la").click() #navigate to homepage with ebay icon on left-top

    SonyLens = "https://www.ebay.com/itm/185643427582"
    fdriver.get(SonyLens) # go for a sony lens

    quantity = fdriver.find_element(By.ID,"qtyTextBox") #quantity bar for ebay
    quantity.click()
    quantity.clear() #clear quantity bar
    quantity.send_keys("2") # write 2 in quantity bar

    print("The title is:" , get_title) #print title

def test_chrome_amazon():

    driver = webdriver.Chrome(chrome_path)
    driver.implicitly_wait(10)

    driver.set_window_size(1000,800)
    driver.get("https://www.amazon.com/ref=nav_logo")
    get_title = driver.title  # getting title
    driver.find_element(By.XPATH, "//img[@alt='Electronics']").click()  # navigate to the Electronics tab
    driver.find_element(By.XPATH, '//*[@id="s-refinements"]/div[1]/ul/li[3]/span/a/span[2]').click()  # # Navigate to the Cars vehicle electronics
    driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(30) > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()  # > to aviation electronics
    driver.find_element(By.XPATH, "//span[contains(text(),'Aircraft Accessories')]").click()   # to the aircraft accessories
    driver.find_element(By.XPATH,'//*[@id="nav-logo-sprites"]').click()   # navigate to homepage

    driver.find_element(By.ID, "twotabsearchtextbox").click()  # click to search bar
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Krzysztof Piatek")  # search for the merch
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)  # click enter

    #### mouse scroll ########
    driver.execute_script("window.scrollBy(0,250)")
    driver.execute_script("window.scrollBy(250,500)")
    driver.execute_script("window.scrollBy(500,750)")
    driver.execute_script("window.scrollBy(750,400)")
    driver.execute_script("window.scrollBy(400,0)")
    ### end of the mouse scroll ####
    driver.find_element(By.XPATH,"""//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span""").click()  # go for the piatek merch

    driver.find_element(By.ID, "twotabsearchtextbox").clear()
    driver.find_element(By.ID, "twotabsearchtextbox").click()  # click to search bar
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("messi")  # search for the merch
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)  # click enter

    driver.get("https://a.co/d/0t9kDFm")  # go for messi merch

    driver.find_element(By.ID, "add-to-cart-button").click()  # add to cart
    driver.find_element(By.ID, "sw-gtc").click()  # go to cart
    driver.find_element(By.ID,"a-autoid-0-announce").click()  # open the quantity selection, look for img/quantitybar_amazon.png
    driver.find_element(By.ID, "quantity_2").click()  # choose the quantity
    driver.find_element(By.ID, "nav-logo-sprites").click()  # navigate to homepage with amazon icon on left-top
    print("The title is:", get_title)  # print title


def test_firefox_amazon():
    fdriver = Firefox(service=service, options=options)
    fdriver.set_window_size(1000,800)
    fdriver.get("https://www.amazon.com/ref=nav_logo")



    get_title = fdriver.title  # getting title
    fdriver.find_element(By.XPATH, "//img[@alt='Electronics']").click()  # navigate to the Electronics tab

    fdriver.find_element(By.XPATH, '//*[@id="s-refinements"]/div[1]/ul/li[3]/span/a/span[2]').click()  # Navigate to the Cars vehicle electronics
    fdriver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(30) > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()  # > to aviation electronics
    fdriver.find_element(By.XPATH, "//span[contains(text(),'Aircraft Accessories')]").click()  # to the aircraft accessories
    fdriver.find_element(By.XPATH,'//*[@id="nav-logo-sprites"]').click()   # navigate to homepage

    fdriver.find_element(By.ID, "twotabsearchtextbox").click()  # click to search bar
    fdriver.find_element(By.ID, "twotabsearchtextbox").send_keys("Krzysztof Piatek")  # search for the merch
    fdriver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)  # click enter

    #### mouse scroll ########
    fdriver.execute_script("window.scrollBy(0,250)")
    fdriver.execute_script("window.scrollBy(250,500)")
    fdriver.execute_script("window.scrollBy(500,750)")
    fdriver.execute_script("window.scrollBy(750,400)")
    fdriver.execute_script("window.scrollBy(400,0)")
    ### end of the mouse scroll ####

    fdriver.get("https://amazon.com/music/player/albums/B07NMHQSYR?marketplaceId=ATVPDKIKX0DER&musicTerritory=US&ref=dm_sh_g4AaivyA9FPmJqK94fR687oUK")

    fdriver.find_element(By.ID, "twotabsearchtextbox").clear()
    fdriver.find_element(By.ID, "twotabsearchtextbox").click()  # click to search bar
    fdriver.find_element(By.ID, "twotabsearchtextbox").send_keys("messi")  # search for the merch
    fdriver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)  # click enter

    fdriver.get("https://a.co/d/0t9kDFm") #go for messi merch

    fdriver.find_element(By.ID, "add-to-cart-button").click() #add to cart
    fdriver.find_element(By.ID, "sw-gtc").click() # go to cart
    fdriver.find_element(By.XPATH, """//*[@id="a-autoid-0-announce"]""").click() #open the quantity selection, look for img/quantitybar_amazon.png
    fdriver.find_element(By.ID, "quantity_2").click() #choose the quantity

    print("The title is:", get_title)  # print title
    fdriver.quit()

#test_chrome_ebay()
#test_firefox_ebay()

#test_chrome_amazon()
#test_firefox_amazon()


