from passphrase import passphrase_menu
from generator import generate_password
from analyzer import check_strength


# ==========================================
# SECUREPASS - PASSWORD SECURITY TOOLKIT
# ==========================================

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def banner():
    print(fr"""
{CYAN}{BOLD}
          /$$$$$$                                                   
        /$$__  $$                                                  
        | $$  \__/  /$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$   /$$$$$$ 
        |  $$$$$$  /$$__  $$ /$$_____/| $$  | $$ /$$__  $$ /$$__  $$
        \____  $$| $$$$$$$$| $$      | $$  | $$| $$  \__/| $$$$$$$$
        /$$  \ $$| $$_____/| $$      | $$  | $$| $$      | $$_____/
        |  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$
        \______/  \_______/ \_______/ \______/ |__/       \_______/
                                                                                                                       
        /$$$$$$$                                                   
        | $$__  $$                                                  
        | $$  \ $$ /$$$$$$   /$$$$$$$ /$$$$$$$                      
        | $$$$$$$/|____  $$ /$$_____//$$_____/                      
        | $$____/  /$$$$$$$|  $$$$$$|  $$$$$$                       
        | $$      /$$__  $$ \____  $$\____  $$                      
        | $$     |  $$$$$$$ /$$$$$$$//$$$$$$$/                      
        |__/      \_______/|_______/|_______/                               
{RESET}
{GREEN}{BOLD}          PASSWORD SECURITY TOOLKIT{RESET}
{WHITE}=================================================={RESET}
""")

# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        banner()

        print(f"""
{CYAN}{BOLD}               MAIN MENU{RESET}

{GREEN}[1]{WHITE} Generate Password
{GREEN}[2]{WHITE} Analyze Password Strength
{GREEN}[3]{WHITE} Generate Passphrase
{RED}[4]{WHITE} Exit

{CYAN}=================================================={RESET}
""")

        choice = input(
            f"{YELLOW}{BOLD}[?] Enter your choice: {RESET}"
        ).strip()

        if choice == "1":
            generate_password()

        elif choice == "2":
            password = input(
                f"{YELLOW}[?] Enter password: {RESET}"
            )

            if password:

                check_strength(password)

            else:

                print(f"{RED}[!] Password cannot be empty.{RESET}")

        elif choice == "3":

            passphrase_menu()
            continue

        elif choice == "4":

            print(f"""
{GREEN}{BOLD}
[+] SecurePass session terminated.
[+] Thank you for using SecurePass!
{RESET}
""")
            break

        else:

            print(f"{RED}[!] Invalid choice. Please select 1-4.{RESET}")

        input(
            f"\n{YELLOW}[*] Press Enter to continue...{RESET}"
        )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()
