# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说名字
    name = scrapy.Field()
    #作者
    author = scrapy.Field()
    #小说地址
    novelurl = scrapy.Field()
    #小说的连载状态
    serialstatus = scrapy.Field()
    #字数
    serialnumber = scrapy.Field()
    #文章类别
    category = scrapy.Field()
    #小说编号
    name_id = scrapy.Field()


class DcontentItem(scrapy.Field):
    #小说编号
    id_name = scrapy.Field()
    #章节内容
    chaptercontent = scrapy.Field()
    #num 绑定章节顺序
    num = scrapy.Field()
    #章节地址
    chapternum = scrapy.Field()
    #章节名字
    chaptername = scrapy.Field()

