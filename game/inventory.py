



inventory = {
    "두쫀쿠": 1,
    "카페라떼": 0
}

def inventory_menu(player_info, inventory):
    while True:
        print("가방을 열었습니다. 어떤 행동을 하시겠습니까?")
        print(f"1. 두쫀쿠사용 (HP + 25) | 수량{inventory['두쫀쿠']}")
        print(f"2. 카페라떼사용 (HP + 25) | 수량{inventory['카페라떼']}")
        print("3. 가방 닫기")
        print("-"*34)
        choice = input("선택:  ")
        if choice == "1":
            if inventory["두쫀쿠"] > 0:
                inventory["두쫀쿠"] -= 1
                player_info["hp"] += 25
                print("두쫀쿠를 사용했습니다! HP가 25 증가했습니다.")
                print("-"*34)
            else:
                print("두쫀쿠가 없습니다.")
                print("-"*34)
        elif choice == "2":
            if inventory["카페라떼"] > 0:
                inventory["카페라떼"] -= 1
                player_info["hp"] += 25
                print("카페라떼를 사용했습니다! HP가 25 증가했습니다.")
                print("-"*34)
            else:
                print("카페라떼가 없습니다.")
                print("-"*34)
        elif choice == "3":
            print("가방을 닫습니다.")
            print("-"*34)
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            print("-"*34)


