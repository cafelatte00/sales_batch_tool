"""
月次・カテゴリ別に売上集計し、Excelに出力するスクリプト。
※参考実装
"""

import os
import pandas as pd
from load_data import load_sales_data


def aggregate_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    月次・カテゴリ別に集計を行う。

    - 年月列を作成（order_date → year_month）
    - 年月 x カテゴリごとに sales, profit, quantity を集計
    """
    df["year_month"] = df["order_date"].dt.to_period("M").astype(str)

    summary = df.groupby(["year_month", "category"]).agg({
        "sales": "sum",
        "profit": "sum",
        "quantity": "sum"
    }).reset_index()

    return summary


if __name__ == "__main__":
    # 元データ読み込み
    df = load_sales_data()

    # 集計処理
    summary_df = aggregate_sales(df)

    # 出力ディレクトリのパス
    output_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "output"))
    os.makedirs(output_dir, exist_ok=True)  # フォルダがなければ作成

    # 出力ファイルのパス
    output_path = os.path.join(output_dir, "sales_summary.xlsx")

    # 結果をエクセルに出力
    summary_df.to_excel(output_path, index=False)

    print("集計結果プレビュー")
    print(summary_df.head())
    print(f"Excelファイルを保存しました：{output_path}")
