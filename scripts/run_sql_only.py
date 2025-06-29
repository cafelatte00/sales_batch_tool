"""
SQLファイルを実行して、集計テーブル monthly_sales_summary を作成する。
"""
import os
from sqlalchemy import create_engine, text
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

# SQLファイル読み込み
with open("sql/aggregate_sales.sql", "r") as file:
    sql_text = file.read()

# ステートメントに分割
sql_statements = [stmt.strip() for stmt in sql_text.split(";") if stmt.strip()]

# 実行（トランザクション管理）
with engine.begin() as conn:
    for stmt in sql_statements:
        conn.execute(text(stmt))

print("SQL集計を実行しました（monthly_sales_summary テーブル作成）")
