from masks import get_mask_card_number
from datetime import datetime


def mask_account_card(string: str) -> tuple[str, str]:
    """ Маскировка номера карты и счета """
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:2])
    number_card_or_score = string_split[-1]

    return name_card_or_score, number_card_or_score


def get_date(inp_inf):
    """Изменение формата даты"""
    date_inf = datetime.strptime(inp_inf[:10], '%Y-%m-%d')
    return f'{date_inf.day:02}.{date_inf.month:02}.{date_inf.year} '


test = "Visa Platinum 7000792289606361"
name_card, card_number = mask_account_card(test)


masked_number = get_mask_card_number(card_number)
print(f"{name_card}: {masked_number}")
print(get_date('2024-03-11T02:26:18.671407'))
