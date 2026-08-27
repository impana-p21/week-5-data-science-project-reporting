import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def basic_analysis(df):
    print("\nDataset Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDescriptive Statistics:")
    print(df.describe(include="all"))


if __name__ == "__main__":
    file_path = "../data/processed/cleaned_dataset.csv"

    df = load_data(file_path)
    basic_analysis(df)
