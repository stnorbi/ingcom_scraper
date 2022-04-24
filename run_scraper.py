from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from IngatlanCom_Scraper.spiders.links_numbers import PhoneNumSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(PhoneNumSpider)
process.start()
