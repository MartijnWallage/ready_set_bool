def map(x: int, y: int) -> float:
    """A function that maps each pair of coordinates onto 
    a float in the interval [0,1]. 
    x and y are in the range [0,2^16)
    Implements the Morton code / Z-order curve, which simply 
    interleaves the bits in the binary representation of x and y.
    """
    if not (0 <= x < (1 << 16) and 0 <= y < (1 << 16)):
        raise ValueError(f"Coordinates out of range: ({x:b}, {y:b})")

    result = 0
    for i in range(16):
        xdigit = (x >> i) & 1
        ydigit = (y >> i) & 1
        result |= xdigit << (i*2 + 1)
        result |= ydigit << (i*2)
    return float(result) / ((1 << 32) - 1)


def main():
    cases = [
        (0,0),
        (0,1),
        (1,0),
        (1,1),
        (0,2),
        (2,0),
        (2,1),
        (1,2),
        (2,2),
        (120,300),
        (2**10-43, 2**13-23),
        (2**16-1, 2**16-1),
    ]

    for case in cases:
        result = map(*case)
        print(f"{case} - ({case[0]:016b}, {case[1]:016b}):\n{result:.32f}\n")


if __name__ == "__main__":
    main()
