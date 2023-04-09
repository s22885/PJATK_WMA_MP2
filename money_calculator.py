def calculate_money(groups, coins_pos, xyposses_tray):
    money_in = 0
    money_all = 0
    for (x, y), group in zip(coins_pos, groups):
        money_all += 500 if group == 1 else 5
        if xyposses_tray['xmin'] < x < xyposses_tray['xmax'] and xyposses_tray['ymin'] < y < xyposses_tray['ymax']:
            money_in += 500 if group == 1 else 5

    return money_in, money_all


