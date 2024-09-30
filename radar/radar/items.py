# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RadarItem(scrapy.Item):
    judul  = scrapy.Field()
    waktu = scrapy.Field()
    


