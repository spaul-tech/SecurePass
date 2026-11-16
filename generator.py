
import secrets
import string

from analyzer import check_strength
from clipboard import copy_to_clipboard, clear_clipboard_after_delay

# Terminal Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"


def generate_password():

    print(f"""
{CYAN}{BOLD}
========================================
          PASSWORD GENERATOR
========================================
{RESET}
""")

    try:

        length = int(input(
            f"{YELLOW}[?] Enter password length (8-64): {RESET}"
        ))

        if length < 8 or length > 64:
            print(f"{RED}[!] Length must be between 8 and 64.{RESET}")
            return

        print(f"""
{CYAN}{BOLD}[+] Select character types:{RESET}

{WHITE}1. Uppercase Letters (A-Z)
2. Lowercase Letters (a-z)
3. Numbers (0-9)
4. Special Symbols (!@#$...)
{RESET}
""")

        use_upper = input(
            f"{YELLOW}[?] Include uppercase? (y/n): {RESET}"
        ).lower().strip() == "y"

        use_lower = input(
            f"{YELLOW}[?] Include lowercase? (y/n): {RESET}"
        ).lower().strip() == "y"

        use_digits = input(
            f"{YELLOW}[?] Include numbers? (y/n): {RESET}"
        ).lower().strip() == "y"

        use_symbols = input(
            f"{YELLOW}[?] Include symbols? (y/n): {RESET}"
        ).lower().strip() == "y"

        character_sets = []

        if use_upper:
            character_sets.append(string.ascii_uppercase)

        if use_lower:
            character_sets.append(string.ascii_lowercase)

        if use_digits:
            character_sets.append(string.digits)

        if use_symbols:
            character_sets.append(string.punctuation)

        if not character_sets:
            print(f"{RED}[!] Select at least one character type.{RESET}")
            return

        if length < len(character_sets):
            print(f"{RED}[!] Password length is too short for selected types.{RESET}")
            return

        # Ensure at least one character from each selected set
        password_chars = [
            secrets.choice(char_set)
            for char_set in character_sets
        ]

        # Combine all selected character sets
        all_chars = "".join(character_sets)

        # Fill remaining password length
        for _ in range(length - len(password_chars)):
            password_chars.append(secrets.choice(all_chars))

        # Securely shuffle the characters
        secrets.SystemRandom().shuffle(password_chars)

        password = "".join(password_chars)

        # Display generated password
        print(f"""
{GREEN}{BOLD}
========================================
          GENERATION SUCCESSFUL
========================================
{RESET}
{WHITE}[PASSWORD]{RESET}

{GREEN}{BOLD}{password}{RESET}

{CYAN}----------------------------------------
{WHITE}[+] Length      : {GREEN}{length}
{WHITE}[+] Uppercase   : {GREEN}{'Yes' if use_upper else 'No'}
{WHITE}[+] Lowercase   : {GREEN}{'Yes' if use_lower else 'No'}
{WHITE}[+] Numbers     : {GREEN}{'Yes' if use_digits else 'No'}
{WHITE}[+] Symbols     : {GREEN}{'Yes' if use_symbols else 'No'}
{CYAN}----------------------------------------{RESET}
""")

        # Analyze generated password
        print(f"\n{CYAN}{BOLD}[*] PASSWORD SECURITY ANALYSIS{RESET}\n")

        check_strength(password)

        # Clipboard option
        copy_choice = input(
            f"\n{YELLOW}[?] Copy password to clipboard? (y/n): {RESET}"
        ).strip().lower()

        if copy_choice == "y":

            if copy_to_clipboard(password):
                print(f"{GREEN}[+] Password copied successfully!{RESET}")
                clear_clipboard_after_delay(password, 30)

            else:
                print(f"{RED}[!] Clipboard operation failed.{RESET}")

    except ValueError:
        print(f"{RED}[!] Please enter a valid number.{RESET}")


if __name__ == "__main__":
    generate_password()
