from ex10 import morton_map

def reverse_map(f: float) -> tuple[int, int]:
    """Decode morton_map by de-interleaving."""
    if not 0 <= f <= 1:
        raise ValueError(f"Input not in [0,1]: {f}")

    bit_rep: int = int(f * ((1 << 32) - 1))
    x = y = 0
    for i in range(16):
        x |= ((bit_rep >> (2*i + 1)) & 1) << i
        y |= ((bit_rep >> (2*i)) & 1) << i
    
    return (x, y)


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
        print(f"Morton of\t{case} is\t{morton:.32f}")
        result = reverse_map(morton)
        print(f"Reverse is\t{result}")
        new_morton = morton_map(*result)
        print(f"Morton of that is\t{new_morton:.32f}")
        new_result = reverse_map(new_morton)
        print(f"Reverse of that is\t{new_result}\n")


if __name__ == "__main__":
    main()

