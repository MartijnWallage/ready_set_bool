from ex10 import morton_map

def reverse_map(n: float) -> tuple[int, int]:
    """Decode morton_map by de-interleaving."""
    if not 0 <= n <= 1:
        raise ValueError(f"Input not in [0,1]: {n}")

    bit_rep: int = int(n * ((1 << 32) - 1))
    x = y = 0
    for i in range(16):
        x |= ((bit_rep >> (2*i + 1)) & 1) << i
        y |= ((bit_rep >> (2*i)) & 1) << i
    
    return (x, y)


# For testing:
from utils import check

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
        morton = morton_map(*case)
        reverse = reverse_map(morton)
        morton2 = morton_map(*reverse)
        print(f"Is reverse_map(morton_map{case}) == {case}?")
        check(reverse == case, f"Expected {case}, got {reverse}")
        print(f"Is morton_map(reverse_map({morton})) == {morton}?")
        check(morton2 == morton, f"Expected {morton}, got {morton2}")
        print()


if __name__ == "__main__":
    main()

