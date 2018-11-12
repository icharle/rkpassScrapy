# -*- coding: utf-8 -*-

# Scrapy settings for rkpass project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'rkpass'

SPIDER_MODULES = ['rkpass.spiders']
NEWSPIDER_MODULE = 'rkpass.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rkpass (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'rkpass.middlewares.RkpassSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'rkpass.middlewares.RkpassDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 上午下载器
   'rkpass.pipelines.QuestionImagePipeline': 300,
   'rkpass.pipelines.OptionAImagePipeline': 301,
   'rkpass.pipelines.OptionBImagePipeline': 302,
   'rkpass.pipelines.OptionCImagePipeline': 303,
   'rkpass.pipelines.OptionDImagePipeline': 304,
   'rkpass.pipelines.sjkMorningPipeline': 305, # 数据库系统工程师
   # 'rkpass.pipelines.xxMorningPipeline': 305, # 信息系统监理师
   # 'rkpass.pipelines.wlMorningPipeline': 305, # 网络工程师
   # 'rkpass.pipelines.RkpassPipeline': 305,  # 软件设计师

   #  下午下载器
   #  'rkpass.pipelines.AfterQuestionImagePipeline': 300,
   #  'rkpass.pipelines.optionAanswerImgPipeline': 301,
   #  'rkpass.pipelines.optionBanswerImgPipeline': 302,
   #  'rkpass.pipelines.optionCanswerImgPipeline': 303,
   #  'rkpass.pipelines.optionDanswerImgPipeline': 304,
   #  'rkpass.pipelines.optionEanswerImgPipeline': 305,
   #  'rkpass.pipelines.AfterPipeline': 306,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MYSQL INFO
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'wx_rkpass'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'root'

# LOG INFO
LOG_LEVEL = 'INFO'

# 图片存储
IMAGES_STORE = './images'