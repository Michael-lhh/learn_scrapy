import scrapy

class BookSpider(scrapy.Spider):

  name = 'books'

  start_urls = ['https://books.toscrape.com/']

  def parse(self, response):

    for book in response.css('article.product_pod'):
        # name = book.xpath('./h3/a/@title').extract_first()
        name = book.css('h3>a::attr(title) ').extract_first()
        price = book.css('p.price_color::text').extract_first()
        status = book.css('p.instock.availability::text').extract()[1].replace(' ', '').replace('\n', ''),
        stars = book.css('article.product_pod p::attr(class)').extract_first().partition(' ')[2],
        yield {
            'name': name,
            'price': price,
            'status': status,
            'stars': stars,
        }

    next_url = response.css('ul.pager li.next a::attr(href)').extract_first()

    if next_url:
      next_url = response.urljoin(next_url)
      yield scrapy.Request(next_url, callback=self.parse)
                    
