from datetime import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    tuple_list = [(item["title"], item["url"]) for item in news]
    return tuple_list


# Requisito 7
def search_by_date(date):
    try:
        iso_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    bd_format_date = "{:%d/%m/%Y}".format(iso_date)
    news = search_news({"timestamp": bd_format_date})
    return [(item["title"], item["url"]) for item in news]


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    tuple_list = [(item["title"], item["url"]) for item in news]
    return tuple_list


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    tuple_list = [(item["title"], item["url"]) for item in news]
    return tuple_list
