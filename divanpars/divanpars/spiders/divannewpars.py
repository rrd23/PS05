import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = [("https://divan.ru")]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lamps = response.css('div.Pk6w8 F15NT')

        for lamp in lamps:
            yield {
                'name': lamp.css('a::text').get(),
                'link': lamp.css('a::attr(href)').get()
            }
            





