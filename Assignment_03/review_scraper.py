import requests, csv
from bs4 import BeautifulSoup
import bs4
import unicodedata
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

driver = webdriver.Firefox(executable_path=r'/Users/richard/Downloads/geckodriver')
driver.get('https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_1?sortBy=recent&pageNumber=1&reviewerType=avp_only_reviews')

for page in list(range(1, 84)):
    data_div = driver.find_element_by_id('cm_cr-review_list')
    data_html = data_div.get_attribute('innerHTML')
    soup = bs4.BeautifulSoup(data_html, "html5lib")
    for item in soup:
        reviews = item.find_all('span', attrs={'data-hook': 'review-body'})
        review = [s.text.strip() for s in reviews]
        review_list.append(review)

        star = item.find_all('i', attrs={'data-hook': 'review-star-rating'})
        rating = [s.text.strip() for s in star]
        rating_list.append(rating)

        dates = item.find_all('span', attrs={'data-hook': 'review-date'})
        date = [s.text.strip() for s in dates]
        date_list.append(date)

        patterns = item.find_all('a', attrs={'data-hook': 'format-strip'})
        pattern = [s.text.strip() for s in patterns]
        pattern_list.append(pattern)

        authors = item.find_all('a', attrs={'data-hook': 'review-author'})
        author = [s.text.strip() for s in authors]
        author_list.append(author)

    next_bar = driver.find_element_by_class_name("a-last")
    next_bar.click()

    normal_delay = random.normalvariate(2, 0.5)
    time.sleep(normal_delay)

def magic(hello):
    new_hello = []
    super_hello = []
    for i in hello:
        new_hello.append('<'.join(i))
    super_hello = '<'.join(new_hello).split('<')
    return super_hello

review_new=magic(review_list)
date_new=magic(date_list)
rating_new=magic(rating_list)
pattern_new=magic(pattern_list)
author_new=magic(author_list)

date_update=[]
for i in date_new:
    b=i.strip(' on')
    date_update.append(b)

rating_update=[]
for i in rating_new:
    b=i[0]
    rating_update.append(b)

pattern_update=[]
for i in pattern_new:
    b=i[9:]
    pattern_update.append(b)

dic={"Date" : date_update,
     "Rating": rating_update,
     "Reviews" : review_new,
     "Pattern": pattern_update,
     "Author": author_new}

df=pd.DataFrame(dic)
df_new=df.set_index("Author")
df.to_json("/Users/richard/Desktop/reviews.json")