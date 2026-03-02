import numpy as np
import pandas as pd


def _print_info(df: pd.DataFrame):
    print(df.info())


def _clean(df: pd.DataFrame) -> pd.DataFrame:
    dfc = df.copy(deep=True)
    # convert date
    dfc["tanggal"] = pd.to_datetime(dfc["tanggal"])
    # get last observation data
    last_date = dfc["tanggal"].max()
    dfc = dfc[dfc["tanggal"] == last_date]
    # normalize data type
    dfc["perlakuan"] = dfc["perlakuan"].astype(str)
    dfc["ulangan"] = dfc["ulangan"].astype(str)
    # get diameter avg
    dfc["diameter"] = dfc[
        [
            "diameter_1",
            "diameter_2",
            "diameter_3",
            "diameter_4",
        ]
    ].mean(axis=1)
    # compute area
    dfc["area"] = np.pi * (dfc["diameter"] / 2) ** 2
    # remove unnecesary data
    dfc = dfc[["perlakuan", "ulangan", "area"]]
    dfc = pd.DataFrame(dfc)
    return dfc


def load() -> pd.DataFrame:
    df = pd.read_csv("../data/fk6b1.csv")
    print("Loaded dataset")
    _print_info(df)
    dfc = _clean(df)
    print("Dataset cleaned")
    _print_info(dfc)
    return dfc
