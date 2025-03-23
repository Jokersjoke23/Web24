def close_far(a, b, c):
    is_b_close = abs(a - b) <= 1
    is_c_close = abs(a - c) <= 1
    is_b_far = abs(a - b) >= 2 and abs(c - b) >= 2
    is_c_far = abs(a - c) >= 2 and abs(b - c) >= 2
    
    return (is_b_close and is_c_far) or (is_c_close and is_b_far)