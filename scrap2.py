from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class StackItem(Item):
       tag = Field()

class StackCrawler(CrawlSpider):
  name = "CrawlerStack"
  start_urls = ['https://es.stackoverflow.com/users/']
  allowed_domains = ['es.stackoverflow.com']



  rules={
      Rule(LinkExtractor(allow=r'tab=tags')),
      Rule(LinkExtractor(allow=r'/users'), callback = 'parse_items')
      }

  def parse_items(self, response):
      item = ItemLoader(StackItem(), response)
      soup = BeautifulSoup(response.body)
      contenido = soup.find(class_="user-tags")

      t_contenido = contenido.text
      item.add_value('tag', t_contenido)

      yield item.load_item()