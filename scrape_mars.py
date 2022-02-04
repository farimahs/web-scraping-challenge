#!/usr/bin/env python
# coding: utf-8




import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
import pandas as pd

def scrape():

    mars_dict ={}
    


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    


    # scrape the news title and paragraph

    mars_url = 'https://redplanetscience.com/'
    browser.visit(mars_url)
    time.sleep(3)

    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text


    


    browser.quit()


    # In[5]:


    # scrape the featured image url

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    


    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')
    images = soup.find_all('img', class_="headerimage fade-in")


    


    print(soup.prettify())


    


    print (images)


    


    for image in images:
        featured_image_src = image['src']

    featured_image = image_url + featured_image_src
    featured_image


    


    browser.quit()


    


    # Mars Facts

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    


    mars_facts_url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(mars_facts_url)
    tables


    


    tables_df = tables[0]
    mars_facts = tables_df.to_html()
    mars_facts


    


    mars_facts.replace('\n', '')
    print (mars_facts)


    


    # Mars Hemispheres

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    


    hem_url = 'https://marshemispheres.com/'
    browser.visit(hem_url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')
    html_list = soup.find_all('a', class_="itemLink product-item", href= True)
    html_list


    


    list_hem = []

    for item in html_list:
        name = item['href']
        if name not in list_hem and name !='#':
            list_hem.append(name)
    list_hem


    


    img_list=[]
    title_list=[]
    img_dict_list = []


    for item in list_hem:
        url = hem_url + item
        browser.visit(url)
        time.sleep(1)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_src = soup.find_all('img', class_="wide-image")
        for img in img_src:
            src = img['src']
            hem_img_url = hem_url + src
            img_list.append(hem_img_url)
            
        title_img = soup.find('h2', class_="title").get_text()
        title_list.append(title_img)
        
        #Creating a dictionary to store the info
        img_dict ={}
        img_dict['title'] = title_img
        img_dict['img_url'] = hem_img_url        
        img_dict_list.append(img_dict)


    


    img_list


    


    title_list


    


    img_dict_list  


    


    final_dictionary = {"News_Title": news_title, "News_Paragragh": news_p, "Featured_Image": featured_image, "Mars_Facts": mars_facts, "Hemispheres": title_list, "Hemisphere_URLs": img_list}
    final_dictionary


    return mars_dict


    




