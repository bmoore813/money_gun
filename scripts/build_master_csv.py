from typing import List

import pandas as pd

from app.enumerations import StocksFolder

files = {
    "amex": StocksFolder.amex_path.value,
    "nasdaq": StocksFolder.nasdaq_path.value,
    "nyse": StocksFolder.nyse_path.value,
}

if __name__ == "__main__":
    data: List[pd.DataFrame] = []
    for name, file_path in files.items():
        df: pd.DataFrame = pd.read_csv(file_path, dtype=object)
        df["Exchange"] = name
        data.append(df)
    master: pd.DataFrame = pd.concat(data)
    df.to_csv(StocksFolder.master_path.value, index=False)
