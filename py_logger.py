def log(processname, logfile, log, feature):
    if feature == "log":
        from time import strftime
        logtime = strftime("[%Y %A %B %dth %H:%M:%S %p]")
        with open(logfile, "a") as logging:
            logging.write(f"[{processname}]      {logtime}      {log}\n")
    elif feature == "clearask":
        yesorno=input("Do you really want to clear the logfile?: ")
        if yesorno == "Yes" or yesorno == "yes":
            with open(logfile, "w") as logging:
                logging.write(f"")
                print("Cleared.")
        else:
            print("Did not clear.")
            exit()
    elif feature == "clearnoask":
        with open(logfile, "w") as logging:
            logging.write(f"")
