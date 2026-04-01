import map
import player
import inventory
import save

def headle_place_event(player_info, place_name):
    if place_name == "학생회관":
        print_line()
        print("학생회관에 도착했습니다. 물전을 구매할수 있습니다.")
        print_line()
        buy = input("물전을 구매하시겠습니까? (Y/N):")
        if buy.lower() == "y":
            print("구매할 물전의 종류를 선택하세요:")
            print("1. 두쫀쿠 - 5000원 (HP + 25)")
            print("2. 카페라떼 - 2500원 (HP + 25)")
            print("3. 구매하지 않음")
            print_line()
            choice = input("선택: ")
            if choice == "1":
                if player_info["money"] >= 5000:
                    player_info["money"] -= 5000
                    # player_info["hp"] += 25
                    print("두쫀쿠를 구매했습니다!")
                    print_line()
                else:
                    print("돈이 부족합니다.")
                    print_line()
            elif choice == "2":
                if player_info["money"] >= 2500:
                    player_info["money"] -= 2500
                    # 
                    print("카페라떼를 구매했습니다!")
                    print_line()
                else:
                    print("돈이 부족합니다.")
                    print_line()
            elif choice == "3":
                print("구매하지 않기로 선택했습니다.")
                print_line()
        
        


def print_line():
    print("-" * 34)

def show_menu():
    print("  1. 상태 보기")
    print("  2. 이동")
    print("  3. 가방 열기")
    print("  4. 저장하기")
    print("  5. 게임 종료")
    print("=" * 34)

def game_title():
     print("\n" + "=" * 34)
     print("        캠퍼스 어드벤처 게임")
     print("=" * 34)



def main():
    player_info = player.creater_player()

    game_title()
    
    while True:
        show_menu()
        choice = input("请输入你的选择: ")
        print_line()


        if choice == "1":
            player.show_status(player_info["hp"], player_info["money"], player_info["time"])
            print(f"현재 위치: {map.get_place_name(player_info['x'], player_info['y'])}")
            print_line()
            


        if  choice == "2":
            place_name = map.get_place_name(player_info['x'], player_info['y'])
            print(f"현재 위치: {place_name}")

            direction = input("이동할 방향을 입력하세요 (북, 남, 서, 동): ")
            x, y, moved = map.move_player(map.GAME_MAP, player_info['x'], player_info['y'], direction)
            if moved:
                player_info['x'], player_info['y'] = x, y

            player.decrease_hp(player_info, 1)

            place_name = map.get_place_name(player_info['x'], player_info['y'])
            print(f"이동한 후 위치: {place_name}")
            headle_place_event(player_info, place_name)
            print_line()
            
            if not moved:
                print("그 방향으로 이동할 수 없습니다. 다시 시도하세요.")
                print_line()
        
            print("이동에 성공했습니다!")
            print_line()

        elif choice == "3":
            inventory.inventory_menu(player_info, inventory.inventory)
            print_line()

        elif choice == "4":
            save.save_game(player_info)
            print("게임이 저장되었습니다.")
            print_line()


        elif choice == "5":
            print("게임을 종료합니다.")
            break

        if player_info["hp"] <= 0:
            print("체력이 0이 되었습니다. 게임 오버!")
            break



if __name__ == "__main__":
    main()
