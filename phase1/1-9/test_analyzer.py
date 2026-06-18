from datetime import date

from analyzer import pv_by_category, total_pv
from models import Article

test_articles = [
    Article(
        article_id=1001,
        title="Pythonで始めるデータ分析入門",
        category="Technology",
        pv=1500,
        avg_time_sec=120,
        published_at=date(2026, 1, 15),
    ),
    Article(
        article_id=1002,
        title="2026年絶対に行きたい日本の秘境10選",
        category="Travel",
        pv=4200,
        avg_time_sec=210,
        published_at=date(2026, 2, 20),
    ),
    Article(
        article_id=1003,
        title="初心者向け！10分で作れる時短ヘルシーレシピ",
        category="Food",
        pv=850,
        avg_time_sec=95,
        published_at=date(2026, 3, 5),
    ),
    Article(
        article_id=1004,
        title="効率的なリモートワークのためのデスク環境構築",
        category="Gadget",
        pv=2300,
        avg_time_sec=180,
        published_at=date(2026, 4, 12),
    ),
    Article(
        article_id=1005,
        title="週末の読書におすすめの本格ミステリー小説",
        category="Books",
        pv=610,
        avg_time_sec=75,
        published_at=date(2026, 5, 1),
    ),
    # Technology を重複させて「同一カテゴリの合算」を検証できるようにする
    Article(
        article_id=1006,
        title="型ヒント徹底活用ガイド",
        category="Technology",
        pv=2000,
        avg_time_sec=150,
        published_at=date(2026, 6, 1),
    ),
]

# PV降順に並べた期待値（Technology = 1500 + 2000 = 3500）
category_pv_sum: dict[str, int] = {
    "Travel": 4200,
    "Technology": 3500,
    "Gadget": 2300,
    "Food": 850,
    "Books": 610,
}


def test_total_pv():
    assert total_pv(test_articles) == 11460


def test_pv_by_category():
    # 同一カテゴリ（Technology）のPVが合算されているか
    assert pv_by_category(test_articles) == category_pv_sum


def test_pv_by_category_sorted_desc():
    # dict の == はキー・値だけ見て順序を無視するため、順序は keys() で別途検証する
    result = pv_by_category(test_articles)
    assert list(result.keys()) == ["Travel", "Technology", "Gadget", "Food", "Books"]
