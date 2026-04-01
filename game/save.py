import json

def save_game(player_info):
    with open("player_save.txt", "w", encoding="utf-8") as f:
        json.dump(player_info,f, ensure_ascii=False, indent=4)
        








