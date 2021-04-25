# -*- coding: utf-8 -*-
import scrapy

class Cats(scrapy.Item):
    name = scrapy.Field()
    lifespan = scrapy.Field()
    weight = scrapy.Field()
    history        = scrapy.Field()
    behavior       = scrapy.Field()
    look       = scrapy.Field()
    grooming = scrapy.Field()
    nutritrional_needs = scrapy.Field()
    fun_facts = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'cats'
    allowed_domains = ['https://vcahospitals.com']
    start_urls = ['https://vcahospitals.com/know-your-pet/cat-breeds']

    BASE_URL = 'https://vcahospitals.com'

    #def start_requests(self,response):
    #    xpath_in = '//div[@class="content-wrapper callout-list-wrapper"]//a//@href'
    #    urls = response.xpath(xpath_in).getall()
    #    urls = ['https://vcahospitals.com' + url for url in urls]
    #    for url in urls:
    #        print(url)
    #        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//div[@class="content-wrapper callout-list-wrapper"]//a//@href').getall()
        for link in links:
            absolute_url = self.BASE_URL + link
            print(absolute_url)
            yield scrapy.Request(absolute_url, callback=self.parse_attr, dont_filter=True)

    def parse_attr(self, response):
        p = Cats()

        name_xpath = '//*[@id="Main"]/article/div/header/h1/text()'
        lifespan_xpath = '//p[@class="life-span"]/strong/text()'
        weight_xpath = '//p[@class="weight"]/strong/text()'
        history_xpath        = '//div[@class="rich-text-panel"]/ul[1]//li//text()'
        behavior_xpath       = '//div[@class="rich-text-panel"]/ul[2]//li//text()'
        look_xpath       = '//div[@class="rich-text-panel"]/ul[3]//li//text()'
        grooming_xpath = '//div[@class="rich-text-panel"]/ul[4]//li//text()'
        if response.xpath('//div[@class="rich-text-panel"]/ul[6]//li//text()').getall()==[]:
            nutritrional_needs_xpath = '//div[@class="rich-text-panel"]/p//text()'
            fun_facts_xpath = '//div[@class="rich-text-panel"]/ul[5]//li//text()'
        else:
            nutritrional_needs_xpath = '//div[@class="rich-text-panel"]/ul[5]//li//text()'
            fun_facts_xpath = '//div[@class="rich-text-panel"]/ul[6]//li//text()'

        history_text = ' '.join(response.xpath(history_xpath).getall())
        behavior_text = ' '.join(response.xpath(behavior_xpath).getall())
        look_text = ' '.join(response.xpath(look_xpath).getall())
        grooming_text = ' '.join(response.xpath(grooming_xpath).getall())
        nutritrional_needs_text = ' '.join(response.xpath(nutritrional_needs_xpath).getall())
        fun_facts_text = ' '.join(response.xpath(fun_facts_xpath).getall())
        name = response.xpath(name_xpath).get()
        lifespan = response.xpath(lifespan_xpath).get()
        weight = response.xpath(weight_xpath).get()

        p['name'] = name
        p['lifespan'] = lifespan
        p['weight'] = weight
        p['history']        = '"' + history_text + '"'
        p['behavior']       = '"' + behavior_text + '"'
        p['look']       = '"' + look_text + '"'
        p['grooming'] = '"' + grooming_text+ '"'
        p['nutritrional_needs'] = '"' + nutritrional_needs_text + '"'
        p['fun_facts'] = '"' + fun_facts_text + '"'

        yield p