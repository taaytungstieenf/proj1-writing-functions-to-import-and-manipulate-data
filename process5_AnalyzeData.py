import pandas as pd
from process3_CombineFilesTogether import combine_files_together


def analyze_data(x):
    """
    Analyze player data attributes

    Args
        x: dataframe

    Returns:
        percent_a (float): percentage of elite player
        percent_b (float): percentage of good player
        percent_c (float): percentage of average player
    """
    count = x['level'].value_counts()

    class_a = count['elite']
    class_b = count['good']
    class_c = count['average']

    total = count.sum()

    percent_a = (class_a / total) * 100
    percent_b = (class_b / total) * 100
    percent_c = (class_c / total) * 100

    return percent_a, percent_b, percent_c
