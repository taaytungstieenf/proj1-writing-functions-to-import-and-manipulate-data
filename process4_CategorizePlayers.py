def categorize_rating(x):
    """
    Args:
        x (str): each element in DataFrame's field
    """
    if 10.0 >= float(x) >= 9.5:
        return 'elite'
    elif 9.5 > float(x) >= 7.5:
        return 'good'
    elif 7.5 > float(x) >= 5.0:
        return 'average'
    else:
        return 'not good enough'
