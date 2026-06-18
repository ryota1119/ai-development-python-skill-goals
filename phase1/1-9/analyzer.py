from models import Article


def total_pv(articles: list[Article]) -> int:
    return sum(article.pv for article in articles)


def pv_by_category(articles: list[Article]) -> dict[str, int]:
    result: dict[str, int] = {}
    for article in articles:
        result[article.category] = result.get(article.category, 0) + article.pv

    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
