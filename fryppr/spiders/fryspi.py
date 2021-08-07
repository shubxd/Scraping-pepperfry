import scrapy

class FryPepper(scrapy.Spider):
    name='fry'

    def start_request(self):
        urls = [
            'https://www.pepperfry.com/site_product/search?q=table&as=0&src=os'
        ]

        for url in urls:
            scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        pass