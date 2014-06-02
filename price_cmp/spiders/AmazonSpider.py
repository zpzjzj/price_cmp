import scrapy
import urllib
from price_cmp.items import PriceCmpItem
from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.selector import Selector
from scrapy.http import Request

class AmazonSpider(Spider) :
	name = "amazon"
	page_cnt = 1
	def __init__(self, keyword, page_num = 1, *args, **kwargs):
		super(AmazonSpider, self).__init__(*args, **kwargs)
		self.allowed_domains = ["www.amazon.cn"]
		self.start_urls = ["http://www.amazon.cn"]
		self.keyword = keyword
		self.page_num = int(page_num)

	def parse(self, response):
		return [FormRequest.from_response(response, 
			formdata = {'field-keywords':self.keyword}, 
			callback = self.scrape_url)]

	def scrape_url(self, response):
		next_page = Selector(response).xpath("//a[@class='pagnNext']/@href").extract()
		if(next_page and self.page_cnt < self.page_num) :	# scrape 10 pages
			self.page_cnt = self.page_cnt + 1
			yield Request(next_page[0], self.scrape_url)	# next page

		items = []
		for sel in Selector(response).xpath("//div[@name]") :	# for div that has nid attribute
			print sel.extract()
			a = sel.xpath(".//div[@class='productTitle']/a").pop()
			item = PriceCmpItem()
			item['url'] = a.xpath('@href').extract().pop()
			item['name'] = a.xpath('text()').extract().pop()
			item['price'] = float(sel.xpath(".//div[@class='newPrice']/span/text()").extract()[0].split()[1])
			items.append(item)

		for item in items :
		 	yield item