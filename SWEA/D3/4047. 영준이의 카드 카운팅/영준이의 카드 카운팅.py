# Error 여부 점검 / 1 : 이상 없음, 0 : ERROR
def is_valid_card(card_str):
    temp = []
    for idx in range(0,len(card_str),3):
        # 단어 3개씩 끊어서, temp에 없다면 대입 -> 중복 여부 확인하기 위함
        if card_str[idx:idx+3] in temp:
            return 0
        else:
            temp.append(card_str[idx:idx+3])
        # 카드 종류만 알면 되므로, temp 값들 중 카드 종류만 반환함
    return [component[0] for component in temp]


total_try = int(input())

for trial in range(1,total_try+1):
    card_str = input()
    need_card = {'S' : 13, 'D' : 13, 'H' : 13, 'C' : 13}
    card_list = is_valid_card(card_str)
    if card_list:
        # 반환된 카드 종류에 따라 카드 개수 차감
        for card in card_list:
            need_card[card] -= 1
        print(f'#{trial} {need_card["S"]} {need_card["D"]} {need_card["H"]} {need_card["C"]}')
    else:
        print(f'#{trial} ERROR')
