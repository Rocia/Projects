import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ispy"

    def start_requests(self):
        urls = ['http://Sakthivel.J:Pass@2511@inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)