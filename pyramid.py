def pyramid(num):
    if num > 15 or num < 1:
        return None

    for i in range(1, num + 1):
        row = []
        for j in range(1, i + 1):
            if j == 1:
                row.append(str(j))
                continue
            row.insert(0, str(j))
            row.insert(len(row), str(j))

        padding = " " * ((num * 2) - (i * 2))
        print(padding, end='')
        print(" ".join(row))


num_lines = int(input("Enter the number of the lines: "))
pyramid(num_lines)
