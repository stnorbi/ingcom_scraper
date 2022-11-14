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
from twisted.python import log

load_dotenv()


#redirect logging to system
observer = log.PythonLoggingObserver()
observer.start()


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
                        #'--marionette-port',
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
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 80,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 120,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 130,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 900,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 1000,
     }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
#USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'MUID=; SRCHD=AF=NOFORM; SRCHUID=1; SRCHUSR=; _EDGE_S=SID=; MUIDB=; _SS=SID=; ipv6=; SRCHHPGUSR=;',
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = os.environ['CONCURRENT_REQUESTS']
CONCURRENT_ITEMS=os.environ['CONCURRENT_ITEMS']

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = os.environ['DOWNLOAD_DELAY']
RANDOMIZE_DOWNLOAD_DELAY=os.environ['RANDOMIZE_DOWNLOAD_DELAY']
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = os.environ['CONCURRENT_REQUESTS_PER_DOMAIN']
CONCURRENT_REQUESTS_PER_IP = os.environ['CONCURRENT_REQUESTS_PER_IP']

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = os.environ['TELNETCONSOLE_ENABLED']

REDIRECT_ENABLED = os.environ['REDIRECT_ENABLED']
REACTOR_THREADPOOL_MAXSIZE = os.environ['REACTOR_THREADPOOL_MAXSIZE']
DOWNLOAD_TIMEOUT = os.environ['DOWNLOAD_TIMEOUT']

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
    'scrapy.pipelines.files.FilesPipeline': 1  # For files
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = os.environ['AUTOTHROTTLE_ENABLED']
# The initial download delay
AUTOTHROTTLE_START_DELAY = os.environ['AUTOTHROTTLE_START_DELAY']
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = os.environ['AUTOTHROTTLE_MAX_DELAY']
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = os.environ['AUTOTHROTTLE_TARGET_CONCURRENCY']
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = os.environ['AUTOTHROTTLE_DEBUG']

RETRY_ENABLED = os.environ['RETRY_ENABLED']
RETRY_TIMES = os.environ['RETRY_TIMES']
RETRY_HTTP_CODES = list(os.environ['RETRY_HTTP_CODES'].split(","))

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



LOG_ENABLED=True
LOG_LEVEL = os.environ['LOG_LEVEL']
LOG_ENCODING='UTF-8'
LOG_FILE='ingatlancom_log.txt'
LOG_FORMAT='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_STDOUT=True

#CONNECTION_STRING = os.environ.get('CONNECTION_SRING')


#AWS S3 Storage:

AWS_ACCESS_KEY_ID = os.environ['ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']

#AWS S3 Storage:
FEEDS = {
        's3://ingatlan-com-source/'+ os.environ['DEAL'] + '/' + os.environ['DEAL']+'_'+os.environ['PROPERTY_TYPE']+'_' + os.environ['CITY'] + '_'+ datetime.now().strftime("%Y%m%d_%H%M%S")+'.json': {
        'format': 'jsonlines',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,
    }
}
