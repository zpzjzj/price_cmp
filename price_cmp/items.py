# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item
from scrapy.item import Field

class PriceCmpItem(Item):
    # define the fields for your item here like:
    name = Field()
    url = Field() 
    price = Field()
           
