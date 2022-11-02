# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime

def clean_text(text):
    text=text.strip(u'\u201c'u'\u201d')
    text=text.strip(u'\n')
    text=text.strip(' ')
    text=text.strip()
    return text

class IngatlanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    street_address=Field(input_processor=MapCompose(clean_text),output_processor=TakeFirst())
    price=Field(input_processor=MapCompose(clean_text),output_processor=TakeFirst())
    url=Field(input_processor=MapCompose(clean_text),output_processor=TakeFirst())
    salesman=Field(input_processor=MapCompose(clean_text),output_processor=TakeFirst())
    sid_salesman=Field(input_processor=MapCompose(clean_text),output_processor=TakeFirst())
    #phone_num=Field(input_processor=MapCompose(clean_text),output_processor=TakeFirst())
    iroda=Field(input_processor=MapCompose(clean_text),output_processor=TakeFirst())


