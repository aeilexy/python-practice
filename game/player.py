def creater_player():
    return {
        "x":0,
        "y":0,
        "hp":10,
        "money":50000,
        "time": 11
    }

def show_status(hp, money,time):
    print(f"체력: {hp}\n돈: {money}\n현재시간: {time}시")

def decrease_hp(player, amount):
    player["hp"] -= amount
    return player["hp"]




