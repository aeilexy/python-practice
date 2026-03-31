GAME_MAP = {
    (0, 0): "연대앞 버스정류장",
    (1, 0): "정문",
    (2, 0): "세브란스병원 버스정류장",

     (0, -2): "공학관",
    (1, -2): "백양로2",
    (2, -2): "백주년기념관",

    (0, -1): "공학원",
    (1, -1): "백양로1",
    (2, -1): "공터1",

}

def get_place_name(x, y):
    return GAME_MAP.get((x, y), "알 수 없는 장소")


def move_player(game_map, x, y, direction):
    while True:
        if direction == "북":
            new_x, new_y = x, y - 1
        elif direction == "남":
            new_x, new_y = x, y + 1
        elif direction == "서":
            new_x, new_y = x - 1, y
        elif direction == "동": 
            new_x, new_y = x + 1, y
        else:
            print("잘못된 방향입니다. 다시 시도하세요.")
            return x, y, False      
        if (new_x, new_y) in game_map:
            return new_x, new_y, True
        else:        
            return x, y, False 

