import scrapy
import json, hashlib

class MovieSpider(scrapy.Spider):      
    

    name = 'Movies'

    start_urls = []
    for i in range(1,988):
        start_urls.append('https://www.themoviedb.org/movie?page=%s&language=en' % i)

    def parse(self, response):
        for i in range(len(response.xpath("//div[@class='item poster card']").extract())):
            second_url = response.urljoin(response.xpath("//p[@class='flex']//a[@class='title result']/@href").extract()[i])
            movie_title = response.xpath("//p[@class='flex']//a[@class='title result']/text()").extract()[i].encode('utf-8')
            movie_story = response.xpath("//p[@class='overview']/text()").extract()[i].encode('utf-8')
            item = {}
            x = hashlib.md5(movie_title+movie_story).hexdigest()
            item['MovieId'] = x
            yield scrapy.Request(second_url, meta={'item':item}, callback=self.parse_page2)


    def parse_page2(self, response):
        #with open('D:/movies2.json') as data_file:
        #    data = json.load(data_file)
        item = response.meta['item']
        third_url = response.url[:-12] + '/images/backdrops?language=en'
        
        def extract_with_xpath_one(query):
            return response.xpath(query).extract_first()

        def extract_with_xpath_mul(query):
            return response.xpath(query).extract()
        

        item['Title'] =             extract_with_xpath_one("//meta[@property='og:title']/@content")
        item['Story'] =             extract_with_xpath_one("//meta[@name='description']/@content")
        item['Released'] =          extract_with_xpath_one("//div[@class='title']//span[@class='release_date']/text()")
        item['VidId'] =             extract_with_xpath_one("//a[@class='no_click play_trailer']/@data-id")
        item['Actors'] =            extract_with_xpath_mul("//ol[@class='people scroller']//li//p//a/text()")
        item['Genres'] =            extract_with_xpath_mul("//section[@class='genres right_column']/ul/li/a/text()")
        item['ImgUrls'] =           extract_with_xpath_one("//meta[@property='og:image']/@content")
            
        yield scrapy.Request(third_url, meta={'item':item}, callback=self.parse_page3)


    def parse_page3(self, response):
        item = response.meta['item']
        def extract_with_xpath_mul(query):
            return response.xpath(query).extract()[:5]

        def extract_with_xpath_mul2(query):
            return response.xpath(query).extract()
        if len(response.xpath("//div[@class='image_content']/a/@href").extract()) >= 5:
            item['BackdropUrls'] = extract_with_xpath_mul("//div[@class='image_content']/a/@href")
        else:
            item['BackdropUrls'] = extract_with_xpath_mul2("//div[@class='image_content']/a/@href")
        return item

class MovieSpiderMetascore(scrapy.Spider):      
    

    name = 'Metascore'

    start_urls = []
    start_urls.append('http://www.metacritic.com/movie/')

    def parse(self, response):
        with open('D:/Official-movie-file.json') as data_file:
            data = json.load(data_file)
        for i in range(len(data)):
            movie = '-'.join(data[i]['Title'].split(' '))
            second_url = 'http://www.metacritic.com/movie/%s' % movie
            item = {}
            yield scrapy.Request(second_url, meta={'item':item}, callback=self.parse_page2)
            
    def parse_page2(self, response):
        print 'is this even activated?'
        item['runtime'] = response.xpath('//div[@class="runtime"]//span[position()=2]/text()').extract_first()
        item['metascore'] = response.xpath('//a[@class="metascore_anchor"]//div/text()').extract_first()
        return item
