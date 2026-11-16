import pyperclip
import threading
import time


# ==========================================
#       CLIPBOARD MANAGER
# ==========================================

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def copy_to_clipboard(password):

    try:
        pyperclip.copy(password)
        return True

    except Exception as error:
        print(f"{RED}[!] Clipboard error: {error}{RESET}")
        return False


def clear_clipboard_after_delay(password, delay=30):

    def clear():

        time.sleep(delay)

        try:
            # Clear only if clipboard still contains this password
            if pyperclip.paste() == password:

                pyperclip.copy("")

                print(
                    f"\n{YELLOW}[*] Clipboard automatically cleared.{RESET}"
                )

        except Exception:
            pass

    thread = threading.Thread(target=clear, daemon=True)
    thread.start()
