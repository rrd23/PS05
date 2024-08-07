import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "podushkipars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/podushki/"]

    def parse(self, response):
        products = response.css('[data-testid="product-card"]')

        parsed_data = []
        for product in products:
            try:
                title = product.css('[itemprop="name"]::text').get()
                price = product.css('[itemprop="price"]::attr(content)').get()
                link = product.css('[itemprop="url"]::attr(href)').get()
                parsed_data.append([title, price, link])
            except Exception as e:
                self.logger.error("Произошла ошибка при парсинге: %s", e)

        # Сохранение данных в CSV файл
        with open("podushki.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Ссылка'])
            writer.writerows(parsed_data)

        self.log("Данные сохранены в 'podushki.csv'")

