def adder(a: int, b: int) -> int:
    while b > 0:
        a, b = a^b, (a&b) << 1
    return a


def main():
    pairs = [
        (0,0),
        (0,1),
        (1,0),
        (1,1),
        (1,2),
        (2,1),
        (101,23),
        (12,123),
    ]
    for pair in pairs:
        print(f"{pair[0]} + {pair[1]} =", adder(*pair))


if __name__ == "__main__":
    main()
