import pandas as pd

def detect_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Return rows where column values lie outside the 1.5*IQR range."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    iqr = Q3 - Q1
    lower_bound = Q1 - 1.5 * iqr
    upper_bound = Q3 + 1.5 * iqr
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]
