import os
import pandas as pd
from clean_data import clean_dataframe

def load_sales_data(csv_path="../data/superstore.csv"):
    """
    superstoreのCSVを読み込んで、日付けなどを整形したDataFrameを返す。
    """

    # このスクリプトファイルのあるディレクトリを取得
    base_dir = os.path.dirname(__file__)

    # データファイルの絶対パスを作成
    file_path = os.path.normpath(os.path.join(base_dir, csv_path))

    print("データ読み込み開始：", file_path)

    # CSV読み込み
    # 日付けの列は日付型に変換して読み込み
    # このcsvファイルはutf-8ではなくlatin1が使われているので、それを指定
    df = pd.read_csv(file_path, encoding="latin1", parse_dates=["Order Date", "Ship Date"])

    df = clean_dataframe(df)

    return df


# テスト実行
if __name__ == "__main__":
    df = load_sales_data()
    print(df.head())
    print(df.info())
