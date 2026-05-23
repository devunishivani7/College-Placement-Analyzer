import pandas as pd


def load_data():

    df = pd.read_csv("data.csv")

    return df


def clean_data(df):

    print(df.info())

    print()

    print(df.describe())

    print()

    print(df.isnull().sum())

    print()

    print(df.duplicated().sum())

    print()

    df["Placed"] = df["Placed"].map({
        "Yes":1,
        "No":0
    })

    return df