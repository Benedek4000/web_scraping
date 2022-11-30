# Web Scraping

Web scraping data scraping used for extracting data from websites.

## Extras

### xpath

- exact tag: `/html/body/div/h1`
- tag anywhere: `//h1` or `//div/h1`
- tag within another tag: `//div//h1`
- span tag with class: `//span[@class="title"]`
- id of span tag with class: `//span[@class="title"]/@id`
- text in span tag with class: `//span[@class="title"]/text()`