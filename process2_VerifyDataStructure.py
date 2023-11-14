def verify_data_structure(csv):
    """
    Checks if a CSV has six columns: name, birth_year, nationality, squad_number, preferred_foot, rating

    Args:
            csv (str): csv file's direction

    Returns:
            True (boolean): if csv file has the correct header
            False (boolean): if csv file has the wrong header
    """
    with open(csv) as file:
        first_line = file.readline()
        csv_header = 'legacy_number,full_name,birth_year,nationality,continent,rating\n'

        if first_line == csv_header:
            return True
        else:
            return False
