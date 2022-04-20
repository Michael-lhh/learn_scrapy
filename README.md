# Scrapy

Just Learn and Push

## CSS selector

```html
<h3><a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a></h3>
```

extract title value

response.css('article.product_pod').css('h3 > a::attr(title) ').extract_first()

extract_first(): extract the first node or first text error may happen if deserve msg at second position




