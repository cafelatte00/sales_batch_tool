import os
import pandas as pd
from sqlalchemy import create_engine, Integer, Float, String, DateTime
from load_data import load_sales_data

from dotenv import load_dotenv

# .envファイルのパスを指定（1つ上の階層）
env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=os.path.normpath(env_path))

# .envファイルからDB接続情報を取得
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")


def save_to_postgres(df: pd.DataFrame, table_name: str = "raw_sales_data"):
    """
    DataFrameをPostgresSQLに保存する
    """
    print("DB保存を開始します...")

    column_types = {
        "row_id": Integer(),
        "order_id": String(20),
        "order_date": DateTime(),
        "ship_date": DateTime(),
        "ship_mode": String(20),
        "customer_id": String(20),
        "customer_name": String(100),
        "segment": String(20),
        "country": String(50),
        "city": String(50),
        "state": String(50),
        "postal_code": String(10),
        "region": String(20),
        "product_id": String(20),
        "category": String(30),
        "sub_category": String(30),
        "product_name": String(200),
        "sales": Float,
        "quantity": Integer,
        "discount": Float,
        "profit": Float
    }

    # PostgreSQL接続URLの作成
    db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(db_url)

    # DataFrameをDBへ保存　
    # index=FalseでDataFrameのインデックスを保存しない
    df.to_sql(table_name, engine, if_exists="replace", index=False,dtype=column_types)

    print(f"保存完了：テーブル名 = {table_name}")

# テスト
if __name__ == "__main__":
    df= load_sales_data()
    save_to_postgres(df)
