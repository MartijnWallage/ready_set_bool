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

# For testing:
GREEN = "\033[32m"
RED   = "\033[31m"
RESET = "\033[0m"

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
        print(f"Testing  {case}...")
        morton = morton_map(*case)
        reverse = reverse_map(morton)
        print(f"Morton:  {morton:.32f}")
        print(f"Reverse: {reverse}")
        morton2 = morton_map(*reverse)
        print(f"Morton:  {morton:.32f}")
        print("reverse(morton(x,y)) == (x,y):", end=" ")
        if reverse == case:
            print(f"{GREEN}✓{RESET}")
        else:
            print(f"{RED}✗{RESET}")
        print("morton(reverse(x)) == x:", end=" ")
        if morton2 == morton:
            print(f"{GREEN}✓{RESET}\n")
        else:
            print(f"{RED}✗{RESET}\n")


if __name__ == "__main__":
    main()

