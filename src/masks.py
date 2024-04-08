def mask_card_number(card_number: str) -> str:
    """
    Функция маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры.
    """
    if not card_number or len(card_number) < 10:
        return "Invalid card number"

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Функция маскирует номер счета, оставляя видимыми только последние 4 цифры.
    """
    if not account_number or len(account_number) < 4:
        return "Invalid account number"

    return f"**{account_number[-4:]}"


card_number = input("Введите номер карты: ")
masked_card_number = mask_card_number(card_number)
print(masked_card_number)

account_number = input("Введите номер счета: ")
masked_account_number = mask_account_number(account_number)
print(masked_account_number)


