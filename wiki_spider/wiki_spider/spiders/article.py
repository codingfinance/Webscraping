import scrapy
from selenium import webdriver
from selenium.webdriver.firefox import options

opt = options.Options()
opt.headless = True




class ArticleSpider(scrapy.Spider):

    name = 'article'

    start_urls = ['https://www.ssga.com/us/en/individual/etfs/fund-finder']
    
    def __init__(self):
        self.driver = webdriver.Firefox(options = opt)

    
    def parse(self, response):
        
        self.driver.get(response.url)
        
        
        print(response.css('td').extract()) 

        
            
            