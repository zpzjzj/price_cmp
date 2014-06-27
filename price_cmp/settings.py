# Scrapy settings for price_cmp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'price_cmp'

SPIDER_MODULES = ['price_cmp.spiders']
NEWSPIDER_MODULE = 'price_cmp.spiders'

# ITEM_PIPELINES = ['price_cmp.pipelines.JsonWithEncodingPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'price_cmp (+http://www.yourdomain.com)'
