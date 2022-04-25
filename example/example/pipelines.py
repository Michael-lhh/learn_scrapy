# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ExamplePipeline:
    def process_item(self, item, spider):
        return item


class PriceConverterPipeline(object):

    exchange_rate = 8.5309

    def process_item(self, item, spider):

        price = float(item['price'][1:]) * self.exchange_rate

        item['price'] = 'RMB%.2f' % price

        return item


class DuplicatesPipeline(object):

    def __init__(self):
        self.book_set = set()


    def process_item(self, item, spider):
        name = item['name']

        if name in self.book_set:
            raise DropItem("Duplicate book found: %s" % item)

        self.book_set.add(name)
        return item
