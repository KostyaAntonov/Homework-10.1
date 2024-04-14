def mask_card_number(card_number: str) -> str:
    """
    Маскирует номера карты на звездочки
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номера счета на звездочки
    """
    digits = "".join([i for i in account_number if i.isdigit()])
    return f"**{digits[-4:]}"


def mask_info(info: str) -> str:
    """
    Определяет тип карты и счета
    """
    parts = info.split(" ", 1)
    if len(parts) != 2:
        return "Invalid info"

    if "Счет" in parts[0]:
        masked_number = mask_account_number(parts[1])
    else:
        masked_number = mask_card_number(parts[1])

    return f"{parts[0]} {masked_number}"


card_info = input("Введите тип карты и номер карты: ")
masked_card_info = mask_info(card_info)
print(masked_card_info)

account_info = input("Введите 'Счет' и номер счета: ")
masked_account_info = mask_info(account_info)
print(masked_account_info)
