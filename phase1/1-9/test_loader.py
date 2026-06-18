import csv
from datetime import date

import pytest
from loader import load_articles


@pytest.fixture
def dummy_csv_file(tmp_path):
    csv_path = tmp_path / "articles.csv"

    data: list[list[str]] = [
        ["article_id", "title", "category", "pv", "avg_time_sec", "published_at"],
        [
            "1001",
            "Pythonで始めるデータ分析入門",
            "Technology",
            "1500",
            "120",
            "2026-01-15",
        ],
        [
            "1002",
            "2026年絶対に行きたい日本の秘境10選",
            "Travel",
            "4200",
            "210",
            "2026-02-20",
        ],
        [
            "1003",
            "初心者向け！10分で作れる時短ヘルシーレシピ",
            "Food",
            "850",
            "95",
            "2026-03-05",
        ],
        [
            "1004",
            "効率的なリモートワークのためのデスク環境構築",
            "Gadget",
            "2300",
            "180",
            "2026-04-12",
        ],
        [
            "1005",
            "週末の読書におすすめの本格ミステリー小説",
            "Books",
            "610",
            "75",
            "2026-05-01",
        ],
    ]

    with open(csv_path, mode="w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    yield csv_path


def test_load_articles_count(dummy_csv_file):
    articles = load_articles(dummy_csv_file)

    # 件数テスト
    assert len(articles) == 5


def test_load_articles_type(dummy_csv_file):
    article = load_articles(dummy_csv_file)[0]

    # 型変換テスト
    assert isinstance(article.pv, int)
    assert isinstance(article.published_at, date)
