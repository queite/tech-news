from operator import itemgetter

from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news.sort(key=itemgetter("comments_count", "title"), reverse=True)
    return [(item["title"], item["url"]) for item in news[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


top_5_categories()
