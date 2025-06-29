import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    カラム名変更・型変更などを行うこレンジング作業
    """
    print("列名変更と型変換を実施中...")

    # カラム名をスネークケースに変換
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    df["postal_code"] = df["postal_code"].astype(str)
    df["sales"] = df["sales"].astype(float)
    df["quantity"] = df["quantity"].astype(int)
    df["discount"] = df["discount"].astype(float)
    df["profit"] = df["profit"].astype(float)

    return df
