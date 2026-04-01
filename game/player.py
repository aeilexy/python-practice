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
    if hp <= 10:
        print("상태: 배고픕니다. 음식을 먹어야 합니다.")


def decrease_hp(player, amount):
    player["hp"] -= amount
    return player["hp"]
 