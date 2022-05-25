import os
import ctypes

# Local files
import logger


def is_root() -> bool:
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1

def clear_scrn() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def verify_os() -> None:
    allowed = ['nt', 'posix', 'darwin']

    if os.name.lower() not in allowed:
        OSNotSupported()

def OSNotSupported():
    logger.CRITICAL(f'\n\nOS must be either Windows Or Linux based such as Darwin (MacOS), Ubuntu etc.\n\n')
    sys.exit(1)
