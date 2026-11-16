
import math
import re


# ==========================================
#       PASSWORD STRENGTH ANALYZER
# ==========================================

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"


def check_strength(password):

    score = 0
    suggestions = []

    length = len(password)

    # Character variety
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[^a-zA-Z0-9]", password))

    character_pool = 0

    if has_upper:
        character_pool += 26

    if has_lower:
        character_pool += 26

    if has_digit:
        character_pool += 10

    if has_symbol:
        character_pool += 32

    # Estimate theoretical entropy
    entropy = 0

    if character_pool > 0:
        entropy = length * math.log2(character_pool)

    # Length checks
    if length >= 16:
        score += 2
    elif length >= 12:
        score += 1
    else:
        suggestions.append(
            "Use at least 12 characters, preferably 16 or more."
        )

    # Character variety checks
    if has_upper:
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if has_lower:
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if has_digit:
        score += 1
    else:
        suggestions.append("Add numbers.")

    if has_symbol:
        score += 1
    else:
        suggestions.append("Add special symbols.")

    # Common password detection
    common_passwords = [
        "password",
        "password123",
        "12345678",
        "qwerty",
        "admin",
        "letmein",
        "welcome"
    ]

    is_common = password.lower() in common_passwords

    # Detect simple sequential patterns
    sequences = [
        "1234", "2345", "3456",
        "abcd", "bcde", "cdef",
        "qwerty", "asdf"
    ]

    has_sequence = any(
        sequence in password.lower()
        for sequence in sequences
    )

    # Detect repeated characters
    has_repetition = bool(
        re.search(r"(.)\1{3,}", password)
    )

    # Final classification
    if is_common or has_sequence or has_repetition:
        strength = "WEAK"

    elif entropy < 40:
        strength = "WEAK"

    elif entropy < 60:
        strength = "MODERATE"

    elif entropy < 80:
        strength = "GOOD"

    else:
        strength = "STRONG"

    # Extra suggestions
    if is_common:
        suggestions.append("Avoid commonly used passwords.")

    if has_sequence:
        suggestions.append(
            "Avoid predictable sequences like 1234 or abcd."
        )

    if has_repetition:
        suggestions.append(
            "Avoid repeating the same character many times."
        )

    # Display results
    strength_color = {
        "WEAK": RED,
        "MODERATE": YELLOW,
        "GOOD": CYAN,
        "STRONG": GREEN
    }

    print(f"\n{CYAN}{BOLD}========================================")
    print("         PASSWORD ANALYSIS")
    print(f"========================================{RESET}")

    print(f"\n{WHITE}[+] Length              : {GREEN}{length}")
    print(f"{WHITE}[+] Uppercase           : {GREEN}{has_upper}")
    print(f"{WHITE}[+] Lowercase           : {GREEN}{has_lower}")
    print(f"{WHITE}[+] Numbers             : {GREEN}{has_digit}")
    print(f"{WHITE}[+] Symbols             : {GREEN}{has_symbol}")
    print(f"{WHITE}[+] Theoretical Entropy : {CYAN}{entropy:.2f} bits")

    print(
        f"\n{WHITE}[+] Password Strength   : "
        f"{BOLD}{strength_color[strength]}{strength}{RESET}"
    )

    if suggestions:

        print(f"\n{YELLOW}[!] Security Suggestions:{RESET}")

        for suggestion in suggestions:
            print(f"{YELLOW}    - {suggestion}{RESET}")

    else:
        print(f"\n{GREEN}[+] No basic improvements suggested.{RESET}")

    print(f"\n{MAGENTA}[!] This is a heuristic assessment, not a guarantee")
    print(f"    of resistance to real-world password attacks.{RESET}")
