def calculate_pi():
    pi = 0
    sign = 1
    previous_pi = 0
    consecutive_same_value_count = 0
    iterations = 1

    while consecutive_same_value_count < 5:
        previous_pi = pi
        pi = pi + sign * 4 / (2 * iterations - 1)
        sign = -sign
        if round(previous_pi, 6) == round(pi, 6):
            consecutive_same_value_count += 1
        else:
            consecutive_same_value_count = 0
        iterations += 1

    pi = round(pi, 6)
    return pi

result_pi = calculate_pi()
print("Pi auf 6 Nachkommastellen genau:", result_pi)
