from collections import Counter
from operator import itemgetter

from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news.sort(key=itemgetter("comments_count", "title"), reverse=True)
    return [(item["title"], item["url"]) for item in news[:5]]


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = [item["category"] for item in news]
    count = Counter(categories).most_common(5)
    sorted_categories = sorted(count, key=lambda x: (-x[1], x[0]))
    return [category[0] for category in sorted_categories]
