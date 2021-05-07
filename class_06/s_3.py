# -*- coding: utf-8 -*-
import scrapy

class Painter(scrapy.Item):
    name        = scrapy.Field()
    years_active       = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'musicians'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = Painter()

        name_xpath        = '//div[@class ="fn"]/text()'
        years_active_xpath       = '//span[text()="Years active"]/parent::*/following-sibling::*//text()'
        p['name']        = response.xpath(name_xpath).getall()
        p['years_active'] = response.xpath(years_active_xpath).getall()
        if p['years_active'] == []:
            p['years_active'] = sel.xpath('//th[contains(text(),"active")]/following-sibling::*//text()').getall()
        yield p

