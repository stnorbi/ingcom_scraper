# Scrapy settings for IngatlanCom_Scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()



BOT_NAME = 'IngatlanCom_Scraper'

SPIDER_MODULES = ['IngatlanCom_Scraper.spiders']
NEWSPIDER_MODULE = 'IngatlanCom_Scraper.spiders'

# for chrome driver 
from shutil import which
  
#FIREFOX SETTINGS
SELENIUM_DRIVER_NAME = 'firefox'

os.environ.get('GECKODRIVER_PATH')
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS=[
                        #Firefox capabilities
                        #'marionette=False',
                        '-headless'
                           ]  


#CHROME SETTINGS
# SELENIUM_DRIVER_NAME = 'chrome'
# SELENIUM_DRIVER_EXECUTABLE_PATH = os.environ.get('CHROMEDRIVER_PATH')
# SELENIUM_DRIVER_EXTENSIONS=['Privacy Pass']
# SELENIUM_DRIVER_ARGUMENTS=[
#                         #Chrome capabilities
#                         #'--load-extension={}'.format(os.environ.get('CHROME_EXTENSIONS')),
#                         #'--headless',
#                         # '--proxy-server=136.228.141.154:80',
#                         '--incognito',
#                         '--window-size=1920,1200',
#                         '--no-sandbox',
#                         '--disable-dev-shm-usage',
#                         '--js-flags=--expose-gc',
#                         '--enable-precise-memory-info',
#                         '--disable-popup-blocking',
#                         '--disable-default-apps',
#                         'disable-infobars',
#                         'use-mobile-user-agent',
#                            ]
  
  
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800,
    'IngatlanCom_Scraper.middlewares.IngatlancomScraperDownloaderMiddleware': 500,
     }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
#USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16
CONCURRENT_ITEMS=500

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 80,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    #'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 120,
   'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 130,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':403,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 900,
    "scrapy_selenium_middleware.SeleniumDownloader":451,
    'IngatlanCom_Scraper.middlewares.IngatlancomScraperSpiderMiddleware': 543,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': None,

    'scrapy_deltafetch.DeltaFetch': 100,
}

# DELTAFETCH_ENABLED = True


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'IngatlanCom_Scraper.pipelines.IngatlancomScraperPipeline': 300,
#    'scrapy_redis.pipelines.RedisPipeline': 400,
    's3pipeline.S3Pipeline': 100,   
    'scrapy.pipelines.files.FilesPipeline': 1  # For files
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 0.25
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 128
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



LOG_ENABLED=True
LOG_LEVEL = 'DEBUG'
LOG_ENCODING='UTF-8'
LOG_FILE='ingatlancom_log.txt'
#LOG_FORMAT='%(asctime)s [%(name)s] %(levelname)s: %(message)s'

#CONNECTION_STRING = os.environ.get('CONNECTION_SRING')


#AWS S3 Storage:

AWS_ACCESS_KEY_ID = os.environ['ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']

#AWS S3 Storage:
FEEDS = {
        's3://ingatlan-com-source/'+ os.environ['DEAL'] + '/' + os.environ['DEAL']+'_'+os.environ['PROPERTY_TYPE']+'_' + os.environ['CITY'] + '_'+ datetime.now().strftime("%Y%m%d_%H%M%S")+'.json': {
        #'s3://ingatlan-com-source/'+ os.environ['DEAL'] + '/' + LOG_FILE: {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,
    }
}
