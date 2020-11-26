from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json


class Duplicates:

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['id'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['id'])
            return item


class WhitespacesRemover:
    def process_item(self, item, spider):
        if item['cep_range'][0] == ' ':
            item['cep_range'] = item['cep_range'][1:]
        return item


class JsonlWriter:
    def process_item(self, item, spider):
        with open('{}.jsonl'.format(item['uf']), 'a') as file:
            infos = {
                'localidade': item['local'],
                'faixa de cep': item['cep_range'],
                'id': item['id']
            }

            line = json.dumps(infos) + '\n'
            file.write(line)
            file.close()

        return item
