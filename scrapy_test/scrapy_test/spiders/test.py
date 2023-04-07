import scrapy
from scrapy_test.items import ScrapyTestItem


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["runoob.com"]
    start_urls = (
        'https://www.runoob.com/',
    )
    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'testSpider.middlewares.processAllExceptionRetryMiddleware': 120,
    #     }
    # }

    def parse(self, response):
        filename ="runoob.html"
        filetext ="runoob.txt"
        div = response.css("div.col.middle-column-home div")
        # text=[]
        title = []
        items = []
        text = {}
        for i in div.xpath("//div[contains(@class,'codelist-desktop')]"):

            # title.append(i.css("h2::text").extract())
            item = ScrapyTestItem
            for j in i.css("a"):
                item = ScrapyTestItem()

                name = j.css("h4::text").get()
                link = j.css("a::attr(href)").get()
                info = i.css("strong::text").get()

                item['name'] = name
                item['link'] = link
                item['info'] = info
                items.append(item)
            text[i.css("h2::text").get()] = items

        with open(filetext, "a+") as f:
            for key,value in zip(text.keys(),text.values()):
                f.write(key)
                f.write("\n")
                for i in value:
                    for iValue in i.values():
                        f.write(iValue)
                        f.write("\n")
                    f.write("\n")
                f.write("----------------------------\n")



