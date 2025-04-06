def mask_account_card(string: str) -> tuple[str, str]:
    """ Маскировка номера карты и счета """
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:2])
    number_card_or_score = string_split[-1]

    return name_card_or_score, number_card_or_score


test = "Visa Platinum 7000792289606361"
name_card, card_number = mask_account_card(test)

from masks import get_mask_card_number

masked_number = get_mask_card_number(card_number)
print(f"{name_card}: {masked_number}")