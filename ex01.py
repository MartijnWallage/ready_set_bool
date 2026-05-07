from ex00 import adder


def multiplier(a: int, b: int) -> int:
    result = 0
    i = 0
    while b >> i > 0:
        if (b >> i) & 1:
            result = adder(result, a << i)
        i += 1
    return result


def main():
    cases = [
        (0,0),
        (0,1),
        (1,0),
        (1,1),
        (1,2),
        (2,1),
        (123,13),
        (9,132),
    ]
    for case in cases:
        print(f"{case[0]} * {case[1]} =", multiplier(*case))


if __name__ == "__main__":
    main()
