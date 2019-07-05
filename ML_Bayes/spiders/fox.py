# -*- coding: utf-8 -*-
import scrapy


class FoxSpider(scrapy.Spider):
    name = 'fox'
    allowed_domains = ['www.foxnews.com']
    start_urls = ['https://www.foxnews.com/world', 'https://www.foxnews.com/politics', 'https://www.foxnews.com/us',
                  'https://www.foxnews.com/opinion']

    def parse(self, response):
        types = response.url.split("/")[-1]
        domain = 'https://www.foxnews.com'
        journals_raw = response.css('h4.title a::attr(href)').extract()
        journals = []


        for journal in journals_raw:
            if 'video' in journal:
                continue
            journals.append(journal)
            urls = domain + journal
            yield scrapy.Request(urls, callback= self.parse_journal,meta={'types': types})


    def parse_journal(self, response):
        articles = {}
        articles['title'] = response.css('h1.headline::text').extract_first()
        if articles['title'] != None:
            articles['content'] = response.css('div.article-body p::text').extract()
            articles['type'] = response.meta['types']
            yield articles

