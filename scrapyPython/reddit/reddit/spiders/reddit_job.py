# -*- coding: utf-8 -*-
import scrapy


class RedditJobSpider(scrapy.Spider):
    name = 'reddit_job'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/funny/']

    def parse(self, response):
        print(response.css('a.s1cbwutf-1'))
        print(response.css('a.s1cbwutf-1').extract())
        print(response.css('a.s1cbwutf-1.attr(href)').extract)
