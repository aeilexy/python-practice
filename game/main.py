import map



def show_menu():
    print("\n" + "=" * 34)
    print("        캠퍼스 어드벤처 게임")
    print("=" * 34)
    print("  1. 현재 위치 확인")
    print("  2. 이동")
    print("  3. 게임 종료")
    print("=" * 34)



def main():
    x, y = 0, 0
    while True:
        show_menu()
        choice = input("请输入你的选择: ")
        # if choice == "1":
        if  choice == "2":
            place_name = map.get_place_name(x, y)
            print(f"현재 위치: {place_name}")
            direction = input("이동할 방향을 입력하세요 (북, 남, 서, 동): ")
            x, y, moved = map.move_player(map.GAME_MAP, x, y, direction)
            
            if not moved:
                print("그 방향으로 이동할 수 없습니다. 다시 시도하세요.")
        elif choice == "3":
            print("게임을 종료합니다.")
            break



if __name__ == "__main__":
    main()
