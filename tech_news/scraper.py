import time

import requests
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        headers = {"user-agent": "Fake user-agent"}
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_link = selector.css(".next.page-numbers::attr(href)").get()
    return next_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip(),
        "tags": selector.css(".post-tags li a[rel=tag]::text").getall(),
        "category": selector.css(".label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    blog_content = ""
    links = []
    news = []

    while len(links) < amount:
        blog_content = fetch(url)
        links.extend(scrape_novidades(blog_content))
        url = scrape_next_page_link(blog_content)

    for link in links[:amount]:
        content = fetch(link)
        data = scrape_noticia(content)
        news.append(data)

    create_news(news)
    return news
