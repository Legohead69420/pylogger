print("Welcome to Pylogger 2.0", "\nThis is the most advanced version yet.", "\nIncluding 3 new and easier to use functions", "\nThe only piece of code you need to get started is 'from py_logger import *'", "\nPlace Pylogger in the directory of the folder of your project and boom its in your project(with the aforementioned code)")
def log(processname="Name of the process", logfile="File for logging", log="What you log"):
    if ':' in logfile:
        # import time
        from time import strftime
        # create time string
        logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")
        # open file for log
        with open(logfile, "a") as logging:
            # write log with formatting
            logging.write(f"[{processname}] {logtime}      {log}\n")
    else:
        import os
        os.system("cls")
        print("ERROR CODE: 543. Warning logfile will not enter the desired directory as you did not include the full file path inside of 'logfile'")
        exit()

def clear(ask="Y or N", logfile="File for clearing", log="What you log after the clear", logornot="Y or N"):
    # neccesary librarys
    import os
    from time import strftime
    import time
    if "Y" in ask or "y" in ask:
        # ask for clear
        os.system("cls")
        yesorno=input("Do you really want to clear the logfile?: ")
        if yesorno == "Y" or yesorno == "y":
            # open file for clear
            with open(logfile, "w") as logging:
                logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")
                # write reason
                if "Y" in logornot or "y" in logornot:
                    logging.write(f"File cleared manually at {logtime} with clear reason: {log}\n")
                else:
                    logging.write("")
                os.system("cls")
                print("Cleared.")
                time.sleep(2.5)
                os.system("cls")
        else:
            # did not clear
            print("Did not clear.")
            exit()
    else:
        # open file for clear
        with open(logfile, "w") as logging:
            # write reason
            logging.write(f"File cleared manually at {logtime} with clear reason: {log}\n")

def seperate(logfile="File for seperation", amount="Amount of seperations"):
    # open file for seperation
    with open(logfile, "a") as logging:
        # get amount of seperations
        a=amount
        # for loop through seperations
        for i in range(a):
            logging.write("\n")

def clearlastline(logfile="File for deleting last line"):
    # list to store file lines
    lines = []
    # read file
    with open(logfile, 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()

    # Write file
    with open(logfile, 'w') as fp:
       # iterate each line
       for number, line in enumerate(lines):
           # delete line 5 and 8. or pass any Nth line you want to remove
            # note list index starts from 0
            length=len(lines)
            if number not in [length-1]:
                fp.write(line)
                
