"""
バッチ処理スクリプト。

1. SQL集計（monthly_sales_summary テーブル作成）
2. Excel出力（sales_summary_from_sql.xlsx 生成）
"""

import subprocess
import os

# scripts ディレクトリの絶対パスを取得
scripts_dir = os.path.dirname(__file__)

# 実行対象スクリプトのパス一覧
script_files = [
    "run_sql_only.py",
    "export_summary_to_excel.py"
]

# 順番に実行
for script in script_files:
    script_path = os.path.join(scripts_dir, script)
    print(f"実行中: {script}")
    subprocess.run(["python", script_path], check=True)

print("バッチ処理がすべて完了しました")
