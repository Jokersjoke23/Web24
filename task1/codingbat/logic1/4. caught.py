def caught_speeding(speed, is_birthday):
    limit_offset = 5 if is_birthday else 0
    if speed <= 60 + limit_offset:
        return 0
    elif speed <= 80 + limit_offset:
        return 1
    else:
        return 2