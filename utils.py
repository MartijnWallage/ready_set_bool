GREEN = "\033[32m"
RED   = "\033[31m"
RESET = "\033[0m"


def check(condition: bool, msg: str) -> None:
    assert condition, f"{RED}✗{RESET} {msg}"
    print(f"{GREEN}✓{RESET} {msg}")
