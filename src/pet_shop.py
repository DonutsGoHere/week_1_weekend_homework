# WRITE YOUR FUNCTIONS HERE
from webbrowser import get


def get_pet_shop_name(shop_name):
    return shop_name["name"]


def get_total_cash(cash_total):
    return cash_total["admin"]["total_cash"]


def add_or_remove_cash(cash_total, cash):
    cash_total["admin"]["total_cash"] += cash


def get_pets_sold(total_pets_sold):
    return total_pets_sold["admin"]["pets_sold"]

def get_pets_by_breed(pets, breed):
    total = []

    for pet in pets["pets"]:
        if pet["breed"] == breed:
            total.append(pet)

    return total
    
    