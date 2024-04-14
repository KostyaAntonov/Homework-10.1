def reformat_date(date_string: str) -> str:
    year, month, day = date_string.split("T")[0].split("-")
    return f"{day}.{month}.{year}"


date_string = "2018-07-11T02:26:18.671407"
reformatted_date = reformat_date(date_string)
print(reformatted_date)
