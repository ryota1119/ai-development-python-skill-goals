from dataclasses import dataclass
from datetime import date


@dataclass
class Article:
    article_id: int
    title: str
    category: str
    pv: int
    avg_time_sec: int
    published_at: date
