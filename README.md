# scrapy-iltalehti-kuntavaalit2021

Fetch all from [Iltalehti Kuntavaalit 2021](https://www.iltalehti.fi/kuntavaalit-2021/vaalikone) site

    scrapy crawl kaikki

Fetch single municipality (97=Jyväskylä): 

    scrapy crawl kunta -a id=97

## Requirements

* Python
* [Scrapy](https://scrapy.org/)
