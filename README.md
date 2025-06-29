# 売上集計バッチ処理ツール（Sales Batch Tool）

米国スーパーの売上データを基に、Python・PostgreSQL・SQL を用いて売上データを月次・カテゴリ別に集計し、Excelファイルに出力するバッチ処理ツールです。

## 使用データ
アプリケーションで使用している売上データは、以下のKaggle公開データセットを基にしています。

- 米国のスーパーストアにおける売上情報(Superstore Dataset)
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

---

## 使用技術

- Python 3.12
- pandas
- SQLAlchemy
- psycopg2
- PostgreSQL
- openpyxl
- dotenv

- PostgreSQL

---

## ディレクトリ構成
sales_batch_tool/
├── data/
│   └── superstore.csv                  # 元データ（スーパーの売上情報CSV）
├── output/
│   ├── sales_summary.xlsx              # Pythonで集計・出力されたExcelファイル
│   └── sales_summary_from_sql.xlsx     # SQLで集計・出力されたExcelファイル
├── sql/
│   └── aggregate_sales.sql             # SQLによる月次・カテゴリ別の集計処理
├── scripts/
│   ├── run_all_batch.py                # 一括実行バッチ（SQL実行＋Excel出力）
│   ├── run_sql_only.py                # SQLによる集計実行のみ
│   ├── export_summary_to_excel.py     # 集計済みテーブルをExcelに出力
│   ├── load_data.py                   # データ読み込み＆整形
│   ├── clean_data.py                  # クレンジング（型変換・列名修正）
│   ├── save_to_db.py                  # PostgreSQLに保存
│   └── aggregate_sales.py             # Pythonでの集計＆Excel出力（参考）
├── .env                               # DB接続情報（環境変数）
├── README.md                          # このファイル
└── requirements.txt                   # 必要なPythonパッケージ
