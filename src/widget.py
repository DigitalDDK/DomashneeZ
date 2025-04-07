from masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(all_name_card: str | int) -> str | int:
    """ Маскировка номера карты и счета """
    new_list = all_name_card.split(' ')
    card_num = []
    card_alph = []

    for i in new_list:
        if i.isalpha():
            card_alph.append(i)
        elif i == ' ':
            card_alph.append(i)
        else:
            card_num.append(i)

    name_letter_card = ''.join(card_alph)

    if name_letter_card == "Счет":
        name_number_card = get_mask_account(''.join(card_num))
    else:
        name_number_card = get_mask_card_number(''.join(card_num))

    return f'{name_letter_card} {name_number_card}'


def get_date(inp_inf):
    """Изменение формата даты"""
    date_inf = datetime.strptime(inp_inf[:10], '%Y-%m-%d')
    return f'{date_inf.day:02}.{date_inf.month:02}.{date_inf.year} '


test = "Visa Platinum 7000792289606361"


print(mask_account_card(test))
print(get_date('2024-03-11T02:26:18.671407'))
