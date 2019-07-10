#dart_result = input()
dart_result = "1S2D*3T"
score = [1, 1, 1]
d_index = 0

for i in range(0, 3):
    try:
        num = int(dart_result[d_index:d_index+2])
        d_index += 1
    except Exception as e:
        num = int(dart_result[d_index])

    d_index += 1
    if dart_result[d_index] == 'S':
        score[i] *= num
    elif dart_result[d_index] == 'D':
        score[i] *= pow(num, 2)
    elif dart_result[d_index] == 'T':
        score[i] *= pow(num, 3)

    if (d_index + 1) < len(dart_result):
        if dart_result[d_index + 1] == '*':
            d_index += 1
            score[i] *= 2
            if i != 0:
                score[i - 1] *= 2
        elif dart_result[d_index + 1] == '#':
            d_index += 1
            score[i] *= -1
    d_index += 1

print(sum(score))