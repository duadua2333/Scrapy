# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['555zw.com']
    start_urls = ['https://www.555zw.com/book/12/12196/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
        2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
        """

        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析
        apost_urls = response.css(".dir .acss .ccss a::attr(href)").extract()
        post_urls = list(reversed(apost_urls))
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        next_url = response.css("div#footlinkb a::attr(href)").extract()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        content = response.xpath("//*[@id='content']/text()").extract()
        str = "".join(content)
        str2 = str.replace("[记住网址 www.555zw.com 三五中文网]", "").replace("\r\n\r\n", "\r\n")
        with open('fiction.txt', "a", encoding="utf-8") as f:
            f.write(str2)
        pass