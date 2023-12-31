# Pylogger
This library took me a long time to make

### Press the `code` drop-down menu and click download zip and extract contents to a folder [Install Instructions](#-instructions-for-install)
## Index
* [💪-Support](#-support)
* [📩-How to download it](#-how-to-download-it)
* [🚦-How to start](#-how-to-start)
* [📝-Instructions for install](#-instructions-for-install)
* [📝-Instructions after install](#-instructions-after-install)
## 📩 How to download it
> [!IMPORTANT]
Download the latest release and run the installer
## 🚦-How to start
> [!IMPORTANT]
Run the "py_logger.py" file itself for the instructions

**All functions contain instructions**
To install this library first download the file pylogger.py and put it into the same folder as your projects and in your code do this command(or run the installer and do the inject function(instructions [here](#-instructions-for-install))):
```
from py_logger import *
```
## 💪-Support
If library does not work message support at [pylogge@gmail.com](https://tinyurl.com/mvytfjrj) or join the [Discord](https://discord.gg/ykwwvZD8Uj)
## 📝-Instructions for install
**This is what your terminal should look like:**
```
Would you like a detailed log(press enter if no)(if yes type 'yes'):
```
**This is for debugging ignore it and press `enter`**
**Now your terminal should look like this**
```
Would you like to directly inject the library to a certain file(press enter if no)(type 'yes' if yes):
```
**Now if you want to directly import the library to a file just type `yes` otherwise press `enter`**
> If you press enter thats the end of the instructions just type `y` and press `enter`
**Now your terminal should look like this**
```
Input path for injection(INCLUDE FILE NAME):
```
**Input the file path for injecting import**
**This is the end of installation instructions**

## 📝-Instructions after install
**These are the instructions after you have installed**
# 
**Before doing anything use the `_init_()` function. Example:**
```
_init_("C:/example/example.log", "Example process")
```
**To log something use the `log()` function. Example:**
```
log("C:\example\example.log", "Example log")
```
**To clear the last line use the `clearlastline()` function**
```
clearlastline("C:\example\example.log")
```
**To clear the full log file use the `clear()` function. Example:**
```
clear(ask to clear or not: "Y", "C:\example\example.log", "Example clear log", log the clear or dont: "Y")
```
**To add seperations / newlines to your log file use the `seperate()` function. Example:**
```
seperate("C:\example\example.log", amount of seperations: 5)
```
