import os
import time
os.system("cls")
install_string = []
with open("C:\Py_Stuff\py_logger.py", "r") as install:
    install_string.append(install.read())
delete=input("Would you like to delete the file afterwards(press enter if no)(type yes if yes): ")
if not delete=="":
    if os.path.exists("py_logger.py"):
        os.remove("py_logger.py")
        print("Deleted update file")
    else:
        print("⚠ ERROR: COULD NOT COMPLETE UPDATE DUE TO FILE NOT EXISTING")
else:
    os.system("cls")
    print("Will not delete")
    time.sleep(1.5)
    os.system("cls")
print("Run the installer and in the first input type 'update' afterwards follow the instructions.")
print("Code the installer needs(remove the [ ](square brackets) and ''(quotes)): ")
print(install_string)
input()
os.system("cls")
