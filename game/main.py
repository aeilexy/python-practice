import map

def main():
    x,y = 0,0
    while True:
        place_name = map.get_place_name(x,y)
        print(f"현재 위치: {place_name}")
        direction = input("이동할 방향을 입력하세요 (북, 남, 서, 동): ")
        x,y, moved = map.move_player(map.GAME_MAP, x, y, direction)
        if not moved:
            print("그 방향으로 이동할 수 없습니다. 다시 시도하세요.")
            print("退出按1")
            if input() == "1":
                print("게임을 종료합니다.")
                break



if __name__ == "__main__":
    main()
