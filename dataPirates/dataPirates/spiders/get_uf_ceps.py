from scrapy.selector import Selector
import scrapy
import uuid
import json

from ..items import dataPiratesItem


class Get_uf_ceps(scrapy.Spider):
    name = 'correios'

    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCep.cfm'

    def start_requests(self):
        UFS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT',
               'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO',
               'RR', 'SC', 'SP', 'SE', 'TO']

        for uf in UFS:
            formdata = {
                'UF': uf,
                'pagini': '1',
                'pagfim': '112',
            }
            yield scrapy.FormRequest(
                self.url,
                formdata=formdata,
                meta={'UF': uf, 'formdata': formdata}
            )

    def parse(self, response):
        table_columns = response.xpath('//table[last()]//td').extract()

        # Each line in the table is represented as each 4 elements starting from
        # 0 in table_columns(array), so i create sub arrays agrouping these 4
        # elements.
        all_zone_infos = [table_columns[index*4:(index+1)*4]
                          for index in range(len(table_columns)//4)]

        for info in all_zone_infos:
            local = Selector(text=info[0]).xpath('//text()').extract_first()
            cep_range = Selector(text=info[1]).xpath(
                '//text()').extract_first()
            id = uuid.uuid5(uuid.NAMESPACE_DNS, cep_range).hex

            single_zone_infos = dataPiratesItem()
            single_zone_infos['uf'] = response.meta['UF']
            single_zone_infos['local'] = local
            single_zone_infos['cep_range'] = cep_range
            single_zone_infos['id'] = id

            yield single_zone_infos

        next_page = response.xpath(
            '//a[normalize-space(text()) = "[ Próxima ]"]').extract_first()

        if next_page:
            starting_page = int(response.meta['formdata']['pagini'])
            end_page = int(response.meta['formdata']['pagfim'])

            response.meta['formdata']['pagini'] = str(starting_page + 112)
            response.meta['formdata']['pagfim'] = str(end_page + 112)

            yield scrapy.FormRequest(
                self.url,
                formdata=response.meta['formdata'],
                meta=response.meta
            )
