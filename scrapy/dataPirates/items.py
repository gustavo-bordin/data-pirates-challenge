import scrapy

class dataPiratesItem(scrapy.Item):
    uf = scrapy.Field()
    local = scrapy.Field()
    cep_range = scrapy.Field()
    id = scrapy.Field()
