import os
import time
from colorama import Fore, init, Back

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
import getpass
import sys
import shutil
import stat


def rmv_hdn_fl(func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


init()
color1 = Fore.GREEN
color2 = Fore.RED


def load(version=str):
    cls()
    color = Fore.BLUE
    percent1 = f"{color1}━"
    percent2 = f"{color2}━"
    print(f"{color}Installing version {version} Please wait")
    for i in range(100):
        print(
            ((f"{percent1}" * i) + (f"{percent2}" * (100 - i))) + f"{Fore.CYAN} {i}%",
            end="\r",
            flush=True,
        )
        time.sleep(0.05)
    color = Fore.CYAN
    print(f"{color}Finished installation")
    input()
    cls()
    color = Fore.WHITE


colors = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.MAGENTA,
    Fore.RED,
    Fore.WHITE,
    Fore.YELLOW,
]
cls()
install_v2_1 = "User:ItzWazy"
color = Fore.GREEN
version = ""

cls()
inject = input(
    "Would you like to directly inject the library to a certain file(press enter if no)(type 'yes' if yes): "
)
if not inject == "":
    cls()
    inject = input(
        f"{color}Input path for injection{color2}(INCLUDE FILE NAME):{color} "
    )
    if ":" in inject:
        with open(inject, "r") as og:
            if not "import pylogger" in og.read():
                with open(inject, "r") as original:
                    data = original.read()
                with open(inject, "w") as modified:
                    modified.write("import pylogger\n" + data)
    else:
        cls()
        print(f"{color2}⚠ ERROR: Could not find path")
        exit()
cls()
versionid = f"install_v{version}"
version = "2.1"
versionid = f"install_v{version}"
path = sys.path
path = f"{path[5]}\pylogger"
paths = [
    f"{path}/log_installer.py",
    f"{path}/README.md",
    f"{path}/py-project.toml",
    f"{path}/setup.py",
]
cmd = str(f"del {path}")
os.system(cmd)
time.sleep(2.5)
os.system(f"git clone --depth=1 https://github.com/Legohead69420/pylogger {path}")
try:
    shutil.rmtree(f"{path}\.git", onerror=rmv_hdn_fl)
    shutil.rmtree(f"{path}\__pycache__", onerror=rmv_hdn_fl)
    shutil.rmtree(f"{path}\.github", onerror=rmv_hdn_fl)
except WindowsError:
    pass
for i in paths:
    try:
        os.remove(i)
    except WindowsError:
        pass
cls()
load("2.1")
