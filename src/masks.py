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
