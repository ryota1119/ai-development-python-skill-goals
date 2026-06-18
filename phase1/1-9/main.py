import argparse
import sys
from pathlib import Path

from loader import load_articles
from reporter import print_report


def main() -> None:
    parser = argparse.ArgumentParser(description="コンテンツ閲覧レポートを表示する")
    parser.add_argument("file_path", type=Path, help="csvファイルのパス")
    args = parser.parse_args()

    try:
        articles = load_articles(args.file_path)
        print_report(articles)
    except FileNotFoundError:
        print(f"Error: ファイルが見つかりません → {args.file_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
