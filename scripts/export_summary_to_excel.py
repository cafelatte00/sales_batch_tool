"""
monthly_sales_summary テーブルの内容を Excel に出力する。
"""
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# .env 読み込み
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# DB接続エンジン
db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# テーブル内容を取得
df = pd.read_sql("SELECT * FROM monthly_sales_summary", engine)

# 出力ディレクトリとパス
output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "sales_summary_from_sql.xlsx")

# Excel出力
df.to_excel(output_path, index=False)

print("Excelファイルに保存しました:", output_path)
