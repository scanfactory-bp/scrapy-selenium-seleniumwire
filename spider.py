from typing import List

from scrapy_selenium_seleniumwire import SeleniumRequest
from scrapy import Spider
from scrapy.http import TextResponse
from scrapy.crawler import CrawlerProcess

class BasicSpider(Spider):
    custom_settings = {
        'SELENIUM_DRIVER_NAME': 'chrome',
        'SELENIUM_DRIVER_EXECUTABLE_PATH':
            '/usr/bin/chromedriver',
        'DRIVER_PATH':
            '/usr/bin/chromedriver',
        'SELENIUM_DRIVER_ARGUMENTS':
            ['--headless', '--no-sandbox', '--disable-dev-shm-usage'],
        'DOWNLOADER_MIDDLEWARES':
            {
                'scrapy_selenium_seleniumwire.SeleniumMiddleware': 800
            }
    }

    def __init__(self, urls: List[str]):
        self.start_urls: List[str] = urls

    def parse(self, response: TextResponse):
        driver = response.request.meta.get('driver')

        if driver:
            for request in driver.requests:
                if request.response:
                    # These urls are coming from background requests
                    url = request.url
                    print(url)

                    yield SeleniumRequest(
                        url=url,
                        callback=self.parse,
                        wait_time=4
                    )


        for href in response.xpath("//a/@href").getall():
            yield SeleniumRequest(
                url=response.urljoin(href),
                callback=self.parse,
                wait_time=4
            )

def parametrize_spider(*outer_args, **outer_kwargs):
    class ParameterizedBasicSpider(BasicSpider):
        def __init__(self, *args, **kwargs):
            super().__init__(
                *outer_args, *args, **outer_kwargs, **kwargs
            )

    return ParameterizedBasicSpider

process = CrawlerProcess()
process.crawl(parametrize_spider(["https://scanfactory.io"]))
process.start()