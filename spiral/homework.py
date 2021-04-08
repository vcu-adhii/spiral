def spiralize(number):
    x = 1
    y = 2
    z = 0
    prev_step = 0

    while x <= number ** 2:
        z += x
        x += y
        prev_step += 1
        if prev_step == 4:
            y += 2
            prev_step = 0
    return total


print(spiralize(501))
