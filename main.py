from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class StackItem(Item):
       tag = Field()
       user = Field()

url = 'https://es.stackoverflow.com/users'
id = input('Ingrese una id: ')

class StackCrawler(CrawlSpider):
  name = "CrawlerStack"
  start_urls = [url+id]
  allowed_domains = ['es.stackoverflow.com']

  rules={
      Rule(LinkExtractor(allow=r'page=')),
      Rule(LinkExtractor(allow=r'/users'), callback = 'parse_items')
      }

  def parse_items(self, response):
      item = ItemLoader(StackItem(), response)
      item.add_xpath('tag','//*[@id="top-tags"]/div/div[1]/div/div/div[1]/a[1]/text()')
      item.add_xpath('user','//*[@id="user-card"]/div/div[2]/div/div[1]/div/div[1]/h2/div/text()')
      yield item.load_item()





