def mask_card_or_account(info: str) -> str:
    """
    Определяет тип карты или счета и маскирует числа
    """
    name, number = info.rsplit(' ', 1)

    if "Счет" in name:
        masked_number = "**" + number[-4:]
    else:
        number = number.replace(' ', '')
        masked_number = number[:6] + '*' * 6 + number[12:]
        masked_number = ' '.join([masked_number[i:i + 4] for i in range(0, len(masked_number), 4)])

    return name + ' ' + masked_number


def reformat_date(date_string: str) -> str:
    """
    Возвращает строку с датой в виде 11.07.2018
    """
    year, month, day = date_string.split("T")[0].split("-")
    return f"{day}.{month}.{year}"


date_string = "2018-07-11T02:26:18.671407"
reformatted_date = reformat_date(date_string)
print(reformatted_date)

info = input("Введите тип карты и номер карты или 'Счет' и номер счета: ")
masked_info = mask_card_or_account(info)
print(masked_info)
