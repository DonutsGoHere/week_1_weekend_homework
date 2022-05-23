# WRITE YOUR FUNCTIONS HERE
from webbrowser import get


def get_pet_shop_name(shop_name):
    return shop_name["name"]


def get_total_cash(cash_total):
    return cash_total["admin"]["total_cash"]


def add_or_remove_cash(total_cash, cash):
    return [self.cc_pet_shop]


def add_or_remove_cash(sale_total, cash):
    return sale_total["admin"]["total_cash"] - 10


def get_pets_sold(total_pets_sold):
    return total_pets_sold["admin"]["pets_sold"]


# def increase_pets_sold(pets_sold, num1):
#     return pets_sold["admin"]["pets_sold"](2)


# def get_stock_count(pets):
#     count = []
#     for pet in pets["pets"]:
#         if pet["pets"]["name"] == True:
#             count.append(pet)

#     return count
# print(count)


def get_pets_by_breed(pets, breed):
    total = []

    for pet in pets["pets"]:
        if pet["breed"] == "British Shorthair":
            total.append(pet)

    return total


def get_pets_by_breed(pets, total):
    total = []

    for pet in pets["pets"]:
        if pet["breed"] == "Dalmation":
            total.append(pet)

    return total


def find_pet_by_name():

# red, green, refactor

#  spent many hours on not getting too far.
