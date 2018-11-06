# -*- coding: utf-8 -*-
import scrapy

from reddit.items import RedditItem
class RedditJobSpider(scrapy.Spider):
    name = 'reddit_job'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/funny/']

    def parse(self, response):
        titles = response.css('a.s1cbwutf-1')
        hrefs = response.css('a.s1cbwutf-1').extract()
        scores = response.css('a.s1cbwutf-1.attr(href)').extract()

        for item in zip(titles, hrefs, scores):

            new_item = RedditItem()

            new_item['title'] = item[0]
            new_item['href'] = item[1]
            new_item['score'] = item[2]
            yield new_item