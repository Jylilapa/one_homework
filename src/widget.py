from src.masks import get_mask_card_number
from src.masks import get_mask_account

def mask_account_card(type_and_number:str) -> str:
    divide_string = type_and_number.split(" ")
    type_card = ""
    for i in divide_string:
        if i == "Счет":
            return f"{divide_string[0]} {get_mask_account(divide_string[-1])}"
        else:
            type_card += i
            type_card_name = type_card[:-1]
            return f"{type_card_name} {get_mask_card_number(divide_string[-1])}"



user_input = input()
print(mask_account_card(user_input))