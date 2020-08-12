from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class StackItem(Item):
       id = Field()


class StackCrawler(CrawlSpider):
  name = "Crawler"
  start_urls = ['https://es.stackoverflow.com/users']
  allowed_domains = ['es.stackoverflow.com']


  rules={
      Rule(LinkExtractor(allow=r'page=')),
      Rule(LinkExtractor(allow=r'/users/'), callback = 'parse_items')

      }

  def parse_items(self, response):
      item = ItemLoader(StackItem(), response)
      item.add_xpath('id', '//*[@id="search"]/div/input/@value')
      yield item.load_item()