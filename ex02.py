def gray_code(n: int) -> int:
    return n ^ (n >> 1)


def main():
    for i in range(0,100):
        print(f"{gray_code(i):>8b}")


if __name__ == "__main__":
    main()
