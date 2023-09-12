def select_seat():
    ticket_cnt = 0
    while True:
        select = input("[1]예매하기, [2]종료하기 : ")
        if select == '1':
            if select_seat_num():
                ticket_cnt += 1
        elif select == '2':
            print("예매를 종료합니다.")
            print_seats()
            return ticket_cnt
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


def select_seat_num():
    print_seats()
    seat_num = input("몇 번 좌석을 예매 하시겠습니까? : ")
    if not 0 < int(seat_num) <= 10:
        print(f"{seat_num}번 좌석은 없습니다. 다른 좌석을 선택해주세요.")
        print_seats()
        return False
    elif not seat_numbers[seat_num]:
        seat_numbers[seat_num] = True
        print(f"{seat_num}번 좌석이 예약 완료되었습니다.")
        print_seats()
        return True
    else:
        print(f"{seat_num}번 좌석은 이미 자리가 있습니다. 다른 좌석을 선택해주세요.")
        print_seats()
        return False


def print_seats():
    for i in seat_numbers.values():
        if i: print("[V]", end=" ")
        else: print("[ ]", end=" ")
    print()

TICKET_PRICE = 12000
seat_numbers = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False,
                '9': False, '10': False}

print(f"총 매출액은 {TICKET_PRICE * select_seat()}원 입니다.")
