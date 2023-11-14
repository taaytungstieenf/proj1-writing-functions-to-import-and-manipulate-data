import pandas as pd
from process4_CategorizePlayers import categorize_rating


def manipulate_data(csv_file, position):
    """
    Converts CSV files into a DataFrame, Add new columns

    Args:
        csv_file (str): file's direction
        position (str): position name

    Returns:
        df (DataFrame): A DataFrame with the CSV data and 3 new fields
    """
    csv_format = isinstance(csv_file, str)
    if csv_format:
        df = pd.read_csv(csv_file)
    else:
        raise Exception("`csv_file` expected a string format!")

    df['position'] = position
    df['level'] = df['rating'].apply(categorize_rating)
    return df
