import csv
from datetime import date
from pathlib import Path

from models import Article


def load_articles(filepath: Path) -> list[Article]:
    with open(filepath, "r", encoding="utf-8") as f:
        return [
            Article(
                article_id=int(row["article_id"]),
                title=row["title"],
                category=row["category"],
                pv=int(row["pv"]),
                avg_time_sec=int(row["avg_time_sec"]),
                published_at=date.fromisoformat(row["published_at"]),
            )
            for row in csv.DictReader(f)
        ]
