import scrapy
import urllib
from price_cmp.items import PriceCmpItem
from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.selector import Selector
from scrapy.http import Request

class TaobaoSpider(Spider) :
	name = "taobao"
	page_cnt = 1

	def __init__(self, keyword, page_num = 1, *args, **kwargs):
		super(TaobaoSpider, self).__init__(*args, **kwargs)
		self.allowed_domains = ["s.taobao.com"]
		self.start_urls = ["http://s.taobao.com/search.php"]
		self.keyword = keyword
		self.page_num = int(page_num)

	def parse(self, response):
		return [FormRequest.from_response(response, 
			formdata = {'q':self.keyword.decode("utf-8").encode("gb2312")}, 
			callback = self.scrape_url)]

	def scrape_url(self, response):
		next_page = Selector(response).xpath("//a[@class='page-next']/@href").extract()
		if(next_page and self.page_cnt < self.page_num) :	# scrape 10 pages
			self.page_cnt = self.page_cnt + 1
			yield Request("http://" + self.allowed_domains[0] + next_page[0],
				self.scrape_url)	# next page

		items = []
		for sel in Selector(response).xpath("//div[@nid]") :	# for div that has nid attribute
			a = (sel.xpath('.//h3[@class="summary"]/a[@title]')).pop()
			item = PriceCmpItem()
			item['url'] = a.xpath('@href').extract().pop()
			item['name'] = a.xpath('@title').extract().pop()
			item['price'] = float(sel.xpath(".//div[contains(concat(' ', normalize-space(@class), ' '), ' price ')]/text()").extract()[0])
			items.append(item)

		for item in items :
		 	yield item