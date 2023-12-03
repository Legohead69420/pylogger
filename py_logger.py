def log(processname="Name of the process", logfile="File for logging", log="What you log") -> None:
    'Function for logging. Usage(example):  log("Example process", "C:\example\example.log", "Example log") Uses predetermined time code. Example of time code: [2023 Tuesday November 28 09:31:40 PM]'
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

def clear(ask=bool, logfile="File for clearing", log="What you log after the clear", logornot=bool) -> input():
    'Clears inputted file. Able to ask for user input to actually clear file. Example: ask=True or False, logfile="File for clearing", log="What you log after the clear", logornot=True or False'
    # neccesary librarys
    import os
    from time import strftime
    import time
    if "Y" in ask or "y" in ask or ask == True:
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
            os.system("cls")
            from time import strftime
            logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")
            with open(logfile, "a") as logging:
                logging.write(f"[Clear] {logtime}      Did not clear.\n")
            print("Did not clear.")
            exit()
    else:
        # open file for clear
        with open(logfile, "w") as logging:
            # write reason
            logging.write(f"File cleared manually at {logtime} with clear reason: {log}\n")

def seperate(logfile="File for seperation", amount="Amount of seperations") -> None:
    'Adds newlines to inputted file. Example: seperate(logfile="C:\example\example.log", amount=5)'
    # open file for seperation
    with open(logfile, "a") as logging:
        # get amount of seperations
        a=amount
        # for loop through seperations
        for i in range(a):
            logging.write("\n")

def clearlastline(logfile="File for deleting last line") -> None:
    'Clears last line of inputted file. Example: clearlastline(logfile="C:\example\example.log")'
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
            # note list index starts from 0
            length=len(lines)
            if number not in [length-1]:
                fp.write(line)
                