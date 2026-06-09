# CLAUDE.md

## プロジェクト概要

西日本新聞メディアラボ DXソリューション部・篠原亮太のClaude活用目標の学習・検証用リポジトリ。
claude.aiとClaude Codeを駆使して業務効率化を図ることを目的とする。

## 目標

- claude.aiのコネクタ（Notion/Backlog/Google Drive/Gmail/GitHub）を活用した業務効率化
- Claude CodeのSkill・Plugin・Agentを駆使した開発効率向上
- 作業時間2〜3割削減（前年度比30〜50%削減）

## 技術スタック

- 言語：Python、Ruby、JavaScript
- 関連ツール：Backlog MCP Server、Notion MCP、GitHub連携

## 開発環境

- OS：macOS（Apple Silicon）
- パッケージマネージャ：Homebrew
- Claude Code：v2.1.150（Homebrewインストール）

## ディレクトリ構成

```
learning_basic_python/
├── CLAUDE.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── .venv/
├── phase1/
│   └── 1-1
│       ├── 01_variables.py
│       ├── 02_operators.py
│       └── 03_io.py
├── phase2/
│   └── ...
└── ...
```

- phaseごとにディレクトリを切る
- ファイル名は `01_` のように番号プレフィックスをつける
- 実行: `uv run python phase1/1-1/01_variables.py`

## 学習者プロフィール

- エンジニア歴 4年目（ミドル）
- 経験言語: PHP / Go / Ruby
- パッケージ管理: uv

## 進め方

### 基本サイクル

1. Claude が**カリキュラムに沿って出題 + ヒントを添える**
2. 自分が**コードを書いて貼る**（ファイルに書いてパスを伝えるか、コードを貼る）
3. Claude が**レビュー**する

### 出題ルール（Claude が守ること）

- **カリキュラムの順序を守る**：まだ学んでいない概念（例：クラスはPhase1-6）を前のフェーズで出題しない
- **ファイル名を必ず明示する**：他のディレクトリの命名規則に合わせる（1トピック1ファイル、`01_` のような番号プレフィックス）
- **正解を先に書かない**：ヒントを出して自分でコードを書いてもらう。どうしても詰まったときだけ正解を提示する

### フェーズ完了時にやること

1. Notionチケットの学習メモにサマリを記録し、ステータスを「完了」に更新する
2. `git commit` でコードを保存する

### カリキュラム（Notionチケット連動）

https://app.notion.com/p/AI-Python-372b5337a08b80ca9331d94453544db9?source=copy_linkを参照

カリキュラム全体マップは上記プロジェクトページの「カリキュラム全体マップ」セクションに記載。

## コードを書くときの方針

- Go / Ruby / PHP との差分を意識したコメントを入れる
- 型ヒントは積極的に書く（Day 7 以降は必須）
- 動けばOKではなく、Pythonらしい書き方を意識する

## レビューの視点

コードレビュー時は以下の優先順位で指摘する。

### 必ず指摘する

- 組み込み型名・関数名を変数名に使っている（`int`, `str`, `list`, `sum` など）
- 課題の要件を満たしていない（未実装・出力が違う）
- 無限ループになるバグなど動作上の問題

### 改善として指摘する

- Pythonicでない書き方（課題のテーマに沿った書き方ができていない場合）
  - 例：内包表記の課題なのにforループで書いている
- 使っていない変数が残っている
- デフォルト引数や安全なAPIを使っていない（`get()` など）
- アルゴリズム上の非効率
  - 例：辞書で済む処理をリストの線形探索でやっている
  - 例：同じデータを複数回ループしている（1回にまとめられる）
  - 例：不要なコピーや中間リストを作っている

### 補足として伝える

- より短く・慣用的に書ける別解
- Go / Ruby / PHP との比較で理解が深まるポイント
- 実務で役立つ関連知識（`decimal`, `round()` など）

### レビューしない

- 動作に影響しないスタイルの好み
- Day 7 以前のコードへの型ヒント強制

## Notionチケット管理

- Notionプロジェクト：https://app.notion.com/p/AI-Python-372b5337a08b80ca9331d94453544db9?source=copy_link
- Ticketsデータベース：https://www.notion.so/f2db5337a08b82a08490817d2860a224
- 着手時: ステータスを「進行中」に更新
- Day 完了時: ステータスを「完了」に更新、実施内容のサマリをチケット本文に記録する
- 担当者: ShinoharaRay

## 進め方のルール

- 各フェーズ完了時にNotionチケットをサマリして完了にする
- 詰まったらclaude.aiで壁打ちしてからClaude Codeで実装する

## 関連リンク

- Notionプロジェクト：https://app.notion.com/p/AI-Python-372b5337a08b80ca9331d94453544db9?source=copy_link
- Ticketsデータベース：https://www.notion.so/f2db5337a08b82a08490817d2860a224
