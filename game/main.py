import map
import player

def print_line():
    print("-" * 34)

def show_menu():
    print("  1. 상태 보기")
    print("  2. 이동")
    print("  3. 게임 종료")
    print("=" * 34)

def game_title():
     print("\n" + "=" * 34)
     print("        캠퍼스 어드벤처 게임")
     print("=" * 34)



def main():
    x, y = 0, 0
    game_title()
    player_info = player.creater_player()
    while True:
        show_menu()
        choice = input("请输入你的选择: ")
        print_line()


        if choice == "1":
            player.show_status(player_info["hp"], player_info["money"])
            print(f"현재 위치: {map.get_place_name(x, y)}")
            print_line()
            print_line()
            


        if  choice == "2":
            place_name = map.get_place_name(x, y)
            print(f"현재 위치: {place_name}")
            direction = input("이동할 방향을 입력하세요 (북, 남, 서, 동): ")
            x, y, moved = map.move_player(map.GAME_MAP, x, y, direction)
            player.decrease_hp(player_info, 1)
            print(f"이동한 후 위치: {map.get_place_name(x, y)}")
            print_line()
            
            if not moved:
                print("그 방향으로 이동할 수 없습니다. 다시 시도하세요.")
                print_line()
            else:
                print_line()
                print("이동에 성공했습니다!")



        elif choice == "3":
            print("게임을 종료합니다.")
            break

        if player_info["hp"] <= 0:
            print("체력이 0이 되었습니다. 게임 오버!")
            break



if __name__ == "__main__":
    main()
