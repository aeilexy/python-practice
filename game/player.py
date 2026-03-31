def creater_player():
    return {
        "x":0,
        "y":0,
        "hp":3,
        "money":50000
    }

def show_status(hp, money):
    print(f"체력: {hp}\n돈: {money}")

def decrease_hp(player, amount):
    player["hp"] -= amount
    return player["hp"]




