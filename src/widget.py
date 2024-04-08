def reformat_date(date_string: str) -> str:
    """

    """
    year, month, day = date_string.split('T')[0].split('-')
    return f'{day}.{month}.{year}'


