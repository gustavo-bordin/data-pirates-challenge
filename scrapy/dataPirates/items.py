import scrapy
from scrapytest.tests import Match, Equal, Type, MoreThan, Map, Len, Required


class dataPiratesItem(scrapy.Item):
    uf = scrapy.Field()
    local = scrapy.Field()
    cep_range = scrapy.Field()
    id = scrapy.Field()
