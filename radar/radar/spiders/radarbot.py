import scrapy

class LampungTimurSpider(scrapy.Spider):
    name = 'radarbot'
    start_urls = ['https://radarlampung.disway.id/kategori/515/lampung-timur']

    def parse(self, response):
        # Parse the data you need from the page
        for article in response.css('.media-body.media-content.media-middle a'):
            link = article.css('::attr(href)').get()
            if link:
                yield response.follow(link, self.parse_article)

        # Find the pagination link for the next page
        current_page = response.url.split('/')[-1]
        if current_page.isdigit():
            next_page = int(current_page) + 30
        else:
            next_page = 30
        
        next_page_url = f'https://radarlampung.disway.id/kategori/515/lampung-timur/{next_page}'

        # Check if next page exists
        if response.css('a[rel="next"]'):
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_article(self, response):
        # Extract the content of the article
        judul = response.css('h1.text-black::text').extract(),
        isi = " ".join(response.css('.text-black-1 p::text').extract()),
        waktu = response.css('.text-grey span.date::text').extract()


        for i in zip(judul,waktu,isi):
            scp = {
                'judul':i[0],
                'waktu':i[1],
                'isi':i[2]
            }
            yield scp
