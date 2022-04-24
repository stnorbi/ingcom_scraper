import scrapy
from scrapy.selector.unified import SelectorList
import time
from scrapy import Selector
import os
import json
from IngatlanCom_Scraper.items import IngatlanItem
from scrapy.loader import ItemLoader
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait

from scrapy.spiders import Rule
from dotenv import load_dotenv
load_dotenv()



class PhoneNumSpider(scrapy.Spider):
    name = "PhoneNum"
    mainurl='https://ingatlan.com'

    # redis_key='PhoneNum'
    
    def __init__(self, *args, **kwargs):
        super(PhoneNumSpider, self).__init__(*args, **kwargs)
        
        self.urls ='https://ingatlan.com/lista/elado+' + os.environ['CITY'] + '+' + os.environ['PROPERTY_TYPE']
    
    def start_requests(self):
        
        # for url in self.urls:
        yield SeleniumRequest(url=self.urls, callback=self.pagination
                              )
        
        
        
    def pagination(self,response):
          
        maxpage=response.css('.pagination__page-number').get().split()#.split()
        print(maxpage)
        #j=int(maxpage[4])+1 #utolsó oldalszám
        j=2
        for i in range(1,j): # A 2-est cseréld le "j"-re!!!
            url=self.urls + "?page=" + str(i)

            yield SeleniumRequest(url=url,callback=self.parseLinks)
    
  

    def parseLinks(self, response):
        
        resp=response.css('a.listing__link.js-listing-active-area::attr(href)').extract()
        for i in resp:
            yield SeleniumRequest(url='https://ingatlan.com'+i,callback=self.phonescrape,
                                  #wait_time=5,
                                  #wait_until=phoneparse,
                                  #EC.element_to_be_clickable((By.CSS_SELECTOR,'.contactContainer > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3)'))
                                  )
  
    
    def phonescrape(self,response):
        
        # driver = response.request.meta['driver']
        # driver.get(response.url)


        # time.sleep(1)
        # button = driver.find_element_by_class_name('phoneNumberRevealOverlay')
        # time.sleep(2)
        # button.click()
        # time.sleep(3)
        # page_source=driver.page_source
        # new_selector = Selector(text=page_source)
        
        new_selector = Selector(text=response.body)

        loader=ItemLoader(item=IngatlanItem(), selector=new_selector)
        loader.add_css('address','.address ::text')
        loader.add_css('price','span.fw-bold.fs-5.text-nowrap span ::text')
        # loader.add_css('iroda','.officeName ::text')
        # loader.add_css('salesman','.d-flex align-items-center text-start h-100 my-auto font-family-secondary ::text')

        
        try:
            loader.add_css('sid_salesman','.listingIdentityPart :strong')
        except:
            loader.add_value('sid_salesman','')
            pass
        
        #loader.add_css('phone_num','.number ::text')
        loader.add_value('url',response.url)
        
        
        yield loader.load_item()

# def phoneparse(driver):
#         try:
#             time.sleep(2)
#             closebutton=driver.find_element_by_class_name('close')
#             print(closebutton)
#             closebutton.click()
#             time.sleep(2)
#             print('pop up becsukva')
#         except:
#             pass
        
#         button = driver.find_element_by_class_name('phoneNumberRevealOverlay')
#         time.sleep(0.5)
#         button.click()
#         time.sleep(0.5)
#         return True
