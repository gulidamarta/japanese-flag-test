from argparse import ArgumentError, ArgumentParser


def flag(n):
    width = n * 3 + 2
    height = n * 2 + 2
    str_result = ""

    def mirror(x, mod):
        if x < mod:
            return x
        else:
            return mod - (x % mod + 1)

    for i in range(0, height):
        for j in range(0, width):
            mod_vertical = n + n // 2 + 1
            mod_horizontal = n + 1
            v = (mirror(i, mod_horizontal), mirror(j, mod_vertical))
            taxicab = (mod_horizontal - v[0], mod_vertical - v[1])
            dist = taxicab[0] + taxicab[1] - 1
            if v[0] == 0 or v[1] == 0:
                str_result += '#'
            elif dist == n // 2:
                str_result += '*'
            elif dist < n // 2:
                str_result += '0'
            else:
                str_result += ' '
        str_result += '\n'

    return str_result


def main():
    parser = ArgumentParser()
    number_argument = parser.add_argument("--number", help="Integer even number", type=int)
    args = parser.parse_args()
    if args.number % 2 != 0:
        raise ArgumentError(number_argument, " should be even integer number.")
    print(flag(args.number))


if __name__ == '__main__':
    main()
