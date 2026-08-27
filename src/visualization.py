import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_missing_values_plot(df, output_path):
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("No missing values found.")
        return

    plt.figure(figsize=(10, 6))
    missing.sort_values(ascending=False).plot(kind="bar")

    plt.title("Missing Values by Column")
    plt.xlabel("Columns")
    plt.ylabel("Number of Missing Values")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def create_correlation_heatmap(df, output_path):
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        print("No numeric columns available.")
        return

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    file_path = "../data/processed/cleaned_dataset.csv"

    df = pd.read_csv(file_path)

    create_missing_values_plot(
        df,
        "../visualizations/missing_values.png"
    )

    create_correlation_heatmap(
        df,
        "../visualizations/correlation_heatmap.png"
    )

    print("Visualization generation completed.")
