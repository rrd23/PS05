import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svetilniki/"]

    def parse(self, response):
        divans = response.css('div._Ud0k U4KZV')
        for divan in divans:
            yield {
                'name': divan.css('div.wYUX2 span::text').get(),
                'price': divan.css('div.wYUX2 span::text').get(),
                'link': divan.css('a').attr['href']
            }






