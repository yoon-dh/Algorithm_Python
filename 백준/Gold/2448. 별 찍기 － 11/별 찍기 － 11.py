def star(n):
    if n == 3:
        star_list = [
            [' ', ' ', '*', ' ', ' '],
            [' ', '*', ' ', '*', ' '],
            ['*', '*', '*', '*', '*']
        ]

        return star_list
    else:
        star_list = star(n // 2)
        result = []
        for _ in range(n):
            result.append([' '] * (2 * n - 1))

        for i in range(len(star_list)):
            for j in range(len(star_list[i])):
                result[i][j + n // 2] = star_list[i][j]
                result[i + n // 2][j] = star_list[i][j]
                result[i + n // 2][j + n] = star_list[i][j]

        return result


for i in star(int(input())):
    print(''.join(i))