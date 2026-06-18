from analyzer import pv_by_category
from models import Article


def print_report(articles: list[Article]):
    print("===== コンテンツ閲覧レポート =====")

    # カテゴリ別PVランキング
    categories = pv_by_category(articles)
    print("【カテゴリ別PVランキング】")
    for index, (category, pv) in enumerate(categories.items(), start=1):
        print(f"{index}. {category} {pv:>8,} PV")

    # 人気記事トップ5
    top_articles = sorted(articles, key=lambda article: article.pv, reverse=True)[:5]
    print("人気記事トップ5")
    for index, article in enumerate(top_articles, start=1):
        minutes, seconds = divmod(article.avg_time_sec, 60)
        print(
            f"{index}. {article.pv:>8,} PV {minutes}分{seconds:02d}秒 {article.title}"
        )
