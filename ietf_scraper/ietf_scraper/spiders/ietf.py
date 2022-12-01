import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span.title:text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        author = response.xpath('//span[@class="author-name"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        text = response.xpath('//div[@class="text"]//span/text()').getall()
        address = response.xpath('//span[@class="address"]/text()').get()
        phone = response.xpath('//span[@class="phone"]/text()').get()
        email = response.xpath('//span[@class="email"]/text()').get()
        return {'title':title, 'author': author, 'date': date, 'text': text, 'address': address, 'phone': phone, 'email': email}
