import scrapy
import random, json

class imdbMoviesSpider(scrapy.Spider):      
    

    name = 'imdbMovies'
    with open('D:/WikiTitles.json') as data_file:
        data = json.load(data_file)

    start_urls = []
    for i in data:
        start_urls.append('http://www.imdb.com/title/%s/' % i['imdbId'])
        
    def parse(self, response):
        item = {}
        third_url = response.url + 'mediaindex?refine=still_frame'
        
        def extract_with_xpath_one(query):
            return response.xpath(query).extract_first()
        
        def extract_with_xpath_one_mod(query):
            return response.xpath(query).extract()[1]

        def extract_with_xpath_mul(query):
            return response.xpath(query).extract()
        
        item['Title'] =             extract_with_xpath_one("//div[@class='title_wrapper']/h1/text()")
        item['Story'] =             extract_with_xpath_one("//div[@class='summary_text']/text()")
        item['FullStory'] =         extract_with_xpath_one('//div[@id="titleStoryLine"]/div[@itemprop="description"]/p/text()')
        item['Keywords'] =          extract_with_xpath_mul("//div[@itemprop='keywords']/a/span/text()")
        item['MetaScore'] =         extract_with_xpath_one('//div[@class="titleReviewBarItem"]/a/div/span/text()')
        item['RunTime'] =           extract_with_xpath_one('//time[@itemprop="duration"]/@datetime')         
        item['Released'] =          extract_with_xpath_one('//meta[@itemprop="datePublished"]/@content')
        item['Actors'] =            extract_with_xpath_mul("//td[@itemprop='actor']/a/span/text()")
       #item['Characters'] =        extract_with_xpath_mul("//section[@class='top_billed']/ol/li/p/text()")
        item['Genres'] =            extract_with_xpath_mul('//span[@itemprop="genre"]/text()')
        item['imdbId'] =            extract_with_xpath_one("//meta[@property='pageId']/@content")
        item['tagLine'] =           extract_with_xpath_one_mod("//div[@class='article']/div[@class='txt-block']/text()")
        item['Poster'] =            extract_with_xpath_one('//div[@class="poster"]/a/img/@src')
        random.seed(extract_with_xpath_one("//div[@class='title_wrapper']/h1/text()") + extract_with_xpath_one("//div[@class='summary_text']/text()"))
        item['MovieId'] = int(round(random.random() * 10000000000))
 
        yield scrapy.Request(third_url, meta={'item':item}, callback=self.parse_page2)


    def parse_page2(self, response):
        item = response.meta['item']
        def extract_with_xpath_mul(query):
            return response.xpath(query).extract()

        item['BackdropUrls'] = extract_with_xpath_mul('//div[@class="media_index_thumb_list"]/a/img/@src')
        return item

        
