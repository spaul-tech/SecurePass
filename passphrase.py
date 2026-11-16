
import secrets
import math
from pathlib import Path


WORDLIST_FILE = Path(__file__).with_name("wordlist.txt")

# Terminal Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def load_wordlist():
    """Load and validate the EFF wordlist."""

    try:
        with open(WORDLIST_FILE, "r", encoding="utf-8") as file:
            words = []

            for line in file:
                parts = line.strip().split()

                # EFF entries contain a five-digit code and a word.
                if len(parts) >= 2 and parts[-1].isalpha():
                    words.append(parts[-1].lower())

        words = list(dict.fromkeys(words))

        if len(words) < 2048:
            raise ValueError(
                "Wordlist is too small. Use the EFF Large Wordlist."
            )

        return words

    except FileNotFoundError:
        raise FileNotFoundError(
            "wordlist.txt not found. Download the EFF wordlist first."
        )


def generate_passphrase(word_count=6, separator="-",
                        capitalize=False):
    """Generate a cryptographically secure passphrase."""

    if not 3 <= word_count <= 10:
        raise ValueError("Word count must be between 3 and 10.")

    words = load_wordlist()

    selected_words = [
        secrets.choice(words)
        for _ in range(word_count)
    ]

    if capitalize:
        selected_words = [word.capitalize() for word in selected_words]

    passphrase = separator.join(selected_words)

    return passphrase


def calculate_entropy(word_count):
    """Calculate theoretical passphrase entropy in bits."""

    words = load_wordlist()

    entropy = word_count * math.log2(len(words))

    return entropy




def passphrase_menu():

    while True:

        print(f"""
{CYAN}{BOLD}
========================================
       SECUREPASS PASSPHRASE GENERATOR
========================================
{RESET}
""")

        try:
            word_count = int(input(
                f"{YELLOW}[?] Number of words (3-10): {RESET}"
            ))

            print(f"""
{CYAN}[+] Choose separator:{RESET}
{WHITE}1. Hyphen (-)
2. Underscore (_)
3. Dot (.)
4. Space
{RESET}""")

            separator_choice = input(
                f"{YELLOW}[?] Select option: {RESET}"
            ).strip()

            separators = {
                "1": "-",
                "2": "_",
                "3": ".",
                "4": " "
            }

            if separator_choice not in separators:
                print(f"{RED}[!] Invalid separator choice.{RESET}")
                continue

            capitalize_choice = input(
                f"{YELLOW}[?] Capitalize words? (y/n): {RESET}"
            ).strip().lower()

            capitalize = capitalize_choice == "y"

            passphrase = generate_passphrase(
                word_count,
                separators[separator_choice],
                capitalize
            )

            entropy = calculate_entropy(word_count)

            print(f"""
{GREEN}{BOLD}
========================================
          GENERATION SUCCESSFUL
========================================
{RESET}
{GREEN}[+] Passphrase generated successfully!{RESET}

{WHITE}{BOLD}[PASSPHRASE]{RESET}
{GREEN}{BOLD}{passphrase}{RESET}

{CYAN}----------------------------------------
{WHITE}[+] Words       : {GREEN}{word_count}
{WHITE}[+] Entropy     : {GREEN}{entropy:.2f} bits
{WHITE}[+] Generator   : {GREEN}Python secrets
{CYAN}----------------------------------------{RESET}
""")

        except ValueError as error:
            print(f"{RED}[!] Error: {error}{RESET}")

        except FileNotFoundError as error:
            print(f"{RED}[!] Error: {error}{RESET}")
            return

        print(f"""
{CYAN}{BOLD}
----------------------------------------
{WHITE}1. Generate Another Passphrase
2. Back to Main Menu
----------------------------------------
{RESET}""")

        choice = input(
            f"{YELLOW}[?] Select option: {RESET}"
        ).strip()

        if choice == "1":
            continue

        elif choice == "2":
            return

        else:
            print(f"{RED}[!] Invalid choice. Returning to main menu.{RESET}")
            return


if __name__ == "__main__":
    passphrase_menu()

