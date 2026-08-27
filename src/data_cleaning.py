import pandas as pd


def load_data(file_path):
    """Load the raw dataset."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Perform basic data cleaning."""
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


if __name__ == "__main__":
    input_file = "../data/raw/dataset.csv"
    output_file = "../data/processed/cleaned_dataset.csv"

    data = load_data(input_file)
    cleaned_data = clean_data(data)

    cleaned_data.to_csv(output_file, index=False)

    print("Data cleaning completed.")
    print(f"Rows: {cleaned_data.shape[0]}")
    print(f"Columns: {cleaned_data.shape[1]}")
