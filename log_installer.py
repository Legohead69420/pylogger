import os
import time
from colorama import Fore, init, Back
init()
color1=Fore.GREEN
color2=Fore.RED
def load(version=str):
    os.system("cls")
    color=Fore.BLUE
    percent2 = f"{color1}━━━━━━━━━━"
    percent1 = f"{color2}━━━━━━━━━━"
    print(f"{color}Installing version {version} Please wait")
    print(f"{percent1}{percent1}{percent1}{percent1} {color1}0%")
    time.sleep(1.0)
    os.system("cls")
    print(f"{color}Installing version {version} Please wait")
    print(f"{percent2}{percent1}{percent1}{percent1} {color1}25%")
    time.sleep(1.0)
    os.system("cls")
    print(f"{color}Installing version {version} Please wait")
    print(f"{percent2}{percent2}{percent1}{percent1} {color1}50%")
    time.sleep(1.0)
    os.system("cls")
    print(f"{color}Installing version {version} Please wait")
    print(f"{percent2}{percent2}{percent2}{percent1} {color1}75%")
    time.sleep(1.0)
    os.system("cls")
    print(f"{color}Installing version {version} Please wait")
    print(f"{percent2}{percent2}{percent2}{percent2} {color1}100%")
    time.sleep(1.0)
    os.system("cls")
    color=Fore.CYAN
    print(f"{color}Finished installation")
    input()
    os.system("cls")
    color=Fore.WHITE
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]
os.system("cls")
install_v2_1='print("Welcome to Pylogger 2.1", "\\nThis is the most advanced version yet.", "\\nIncluding 3 new and easier to use functions", "\\nThe only piece of code you need to get started is \'from py_logger import *\'", "\\nPlace Pylogger in the directory of the folder of your project and boom its in your project(with the aforementioned code)")\ndef log(processname="Name of the process", logfile="File for logging", log="What you log"):\n    \'Function for logging. Usage(example):  log("Example process", "C:\\example\\example.log", "Example log")\'\n    if \':\' in logfile:\n        # import time\n        from time import strftime\n        # create time string\n        logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")\n        # open file for log\n        with open(logfile, "a") as logging:\n            # write log with formatting\n            logging.write(f"[{processname}] {logtime}      {log}\\n")\n    else:\n        import os\n        os.system("cls")\n        print("ERROR CODE: 543. Warning logfile will not enter the desired directory as you did not include the full file path inside of \'logfile\'")\n        exit()\n\ndef clear(ask=bool, logfile="File for clearing", log="What you log after the clear", logornot=bool):\n    # neccesary librarys\n    import os\n    from time import strftime\n    import time\n    if "Y" in ask or "y" in ask:\n        # ask for clear\n        os.system("cls")\n        yesorno=input("Do you really want to clear the logfile?: ")\n        if yesorno == "Y" or yesorno == "y":\n            # open file for clear\n            with open(logfile, "w") as logging:\n                logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")\n                # write reason\n                if "Y" in logornot or "y" in logornot:\n                    logging.write(f"File cleared manually at {logtime} with clear reason: {log}\\n")\n                else:\n                    logging.write("")\n                os.system("cls")\n                print("Cleared.")\n                time.sleep(2.5)\n                os.system("cls")\n        else:\n            # did not clear\n            os.system("cls")\n            from time import strftime\n            logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")\n            with open(logfile, "a") as logging:\n                logging.write(f"[Clear] {logtime}      Did not clear.\\n")\n            print("Did not clear.")\n            exit()\n    else:\n        # open file for clear\n        with open(logfile, "w") as logging:\n            # write reason\n            logging.write(f"File cleared manually at {logtime} with clear reason: {log}\\n")\n\ndef seperate(logfile="File for seperation", amount="Amount of seperations"):\n    # open file for seperation\n    with open(logfile, "a") as logging:\n        # get amount of seperations\n        a=amount\n        # for loop through seperations\n        for i in range(a):\n            logging.write("\\n")\n\ndef clearlastline(logfile="File for deleting last line"):\n    # list to store file lines\n    lines = []\n    # read file\n    with open(logfile, \'r\') as fp:\n        # read an store all lines into list\n        lines = fp.readlines()\n\n    # Write file\n    with open(logfile, \'w\') as fp:\n       # iterate each line\n       for number, line in enumerate(lines):\n            # note list index starts from 0\n            length=len(lines)\n            if number not in [length-1]:\n                fp.write(line)\n                '
install_v2_0='print("Welcome to Pylogger 2.0", "\\nThis is the most advanced version yet.", "\\nIncluding 3 new and easier to use functions", "\\nThe only piece of code you need to get started is \'from py_logger import *\'", "\\nPlace Pylogger in the directory of the folder of your project and boom its in your project(with the aforementioned code)")\ndef log(processname="Name of the process", logfile="File for logging", log="What you log"):\n    if \':\' in logfile:\n        # import time\n        from time import strftime\n        # create time string\n        logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")\n        # open file for log\n        with open(logfile, "a") as logging:\n            # write log with formatting\n            logging.write(f"[{processname}] {logtime}      {log}\\n")\n    else:\n        import os\n        os.system("cls")\n        print("ERROR CODE: 543. Warning logfile will not enter the desired directory as you did not include the full file path inside of \'logfile\'")\n        exit()\n\ndef clear(ask="Y or N", logfile="File for clearing", log="What you log after the clear", logornot="Y or N"):\n    # neccesary librarys\n    import os\n    from time import strftime\n    import time\n    if "Y" in ask or "y" in ask:\n        # ask for clear\n        os.system("cls")\n        yesorno=input("Do you really want to clear the logfile?: ")\n        if yesorno == "Y" or yesorno == "y":\n            # open file for clear\n            with open(logfile, "w") as logging:\n                logtime = strftime("[%Y %A %B %d %I:%M:%S %p]")\n                # write reason\n                if "Y" in logornot or "y" in logornot:\n                    logging.write(f"File cleared manually at {logtime} with clear reason: {log}\\n")\n                else:\n                    logging.write("")\n                os.system("cls")\n                print("Cleared.")\n                time.sleep(2.5)\n                os.system("cls")\n        else:\n            # did not clear\n            print("Did not clear.")\n            exit()\n    else:\n        # open file for clear\n        with open(logfile, "w") as logging:\n            # write reason\n            logging.write(f"File cleared manually at {logtime} with clear reason: {log}\\n")\n\ndef seperate(logfile="File for seperation", amount="Amount of seperations"):\n    # open file for seperation\n    with open(logfile, "a") as logging:\n        # get amount of seperations\n        a=amount\n        # for loop through seperations\n        for i in range(a):\n            logging.write("\\n")\n\ndef clearlastline(logfile="File for deleting last line"):\n    # list to store file lines\n    lines = []\n    # read file\n    with open(logfile, \'r\') as fp:\n        # read an store all lines into list\n        lines = fp.readlines()\n\n    # Write file\n    with open(logfile, \'w\') as fp:\n       # iterate each line\n       for number, line in enumerate(lines):\n           # delete line 5 and 8. or pass any Nth line you want to remove\n            # note list index starts from 0\n            length=len(lines)\n            if number not in [length-1]:\n                fp.write(line)\n                \n'
install_v1_0='def log(processname, logfile, log, feature):\n    if feature == "log":\n        from time import strftime\n        logtime = strftime("[%Y %A %B %dth %H:%M:%S %p]")\n        with open(logfile, "a") as logging:\n            logging.write(f"[{processname}]      {logtime}      {log}\\n")\n    elif feature == "clearask":\n        yesorno=input("Do you really want to clear the logfile?: ")\n        if yesorno == "Yes" or yesorno == "yes":\n            with open(logfile, "w") as logging:\n                logging.write(f"")\n                print("Cleared.")\n        else:\n            print("Did not clear.")\n            exit()\n    elif feature == "clearnoask":\n        with open(logfile, "w") as logging:\n            logging.write(f"")\n'
logging=['169.246.137.101 - - [21/Nov/2023:21:25:38 -0500] "PUT /search/tag/list HTTP/1.0" 200 5069 "https://www.murphy.com/posts/tagterms.htm" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/17.0.821.0 Safari/532.0"', '\n', '61.152.8.252 - - [21/Nov/2023:21:28:26 -0500] "GET /wp-admin HTTP/1.0" 200 4958 "https://torres-nelson.biz/app/exploreprivacy.html" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_9; rv:1.9.2.20) Gecko/2069-11-29 01:26:45 Firefox/3.6.15"', '\n', '213.116.141.178 - - [21/Nov/2023:21:32:03 -0500] "GET /search/tag/list HTTP/1.0" 200 4962 "https://crawford-martin.com/wp-content/blog/tagsregister.jsp" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/55.0.815.0 Safari/534.0"', '\n', '100.17.53.205 - - [21/Nov/2023:21:35:33 -0500] "GET /wp-admin HTTP/1.0" 200 4983 "https://taylor.com/categoriessearch.html" "Mozilla/5.0 (iPad; CPU iPad OS 10_3_4 like Mac OS X) AppleWebKit/531.0 (KHTML, like Gecko) CriOS/62.0.888.0 Mobile/09G420 Safari/531.0"', '\n', '135.45.209.188 - - [21/Nov/2023:21:36:24 -0500] "GET /app/main/posts HTTP/1.0" 200 4993 "https://www.hernandez.com/categoriesindex.asp" "Mozilla/5.0 (Windows; U; Windows NT 5.01) AppleWebKit/535.30.5 (KHTML, like Gecko) Version/4.0.3 Safari/535.30.5"', '\n', '140.146.49.86 - - [21/Nov/2023:21:37:22 -0500] "GET /posts/posts/explore HTTP/1.0" 200 4955 "https://reyes-thompson.net/blog/taglogin.html" "Mozilla/5.0 (Android 3.2.1; Mobile; rv:23.0) Gecko/23.0 Firefox/23.0"', '\n', '34.217.156.80 - - [21/Nov/2023:21:38:38 -0500] "GET /explore HTTP/1.0" 200 5036 "https://jackson.com/blog/category/searchregister.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_6 like Mac OS X) AppleWebKit/534.1 (KHTML, like Gecko) FxiOS/12.4q7953.0 Mobile/51C064 Safari/534.1"', '\n', '110.52.50.152 - - [21/Nov/2023:21:39:10 -0500] "GET /posts/posts/explore HTTP/1.0" 200 5033 "http://www.murphy-murray.com/posts/main/mainhomepage.jsp" "Mozilla/5.0 (Windows NT 5.2; sw-KE; rv:1.9.0.20) Gecko/5606-08-15 07:51:22 Firefox/3.6.11"', '\n', '21.42.222.201 - - [21/Nov/2023:21:43:28 -0500] "DELETE /posts/posts/explore HTTP/1.0" 200 5006 "http://stephens-rice.com/app/categories/blogauthor.php" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_0) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/34.0.805.0 Safari/532.2"', '\n', '1.34.78.119 - - [21/Nov/2023:21:45:02 -0500] "GET /posts/posts/explore HTTP/1.0" 200 4965 "http://sutton.info/explorelogin.html" "Mozilla/5.0 (iPad; CPU iPad OS 9_3_5 like Mac OS X) AppleWebKit/533.1 (KHTML, like Gecko) FxiOS/10.0x8135.0 Mobile/21O982 Safari/533.1"', '\n', '201.107.44.239 - - [21/Nov/2023:21:45:58 -0500] "GET /wp-admin HTTP/1.0" 200 4959 "https://www.edwards.com/categoriesmain.jsp" "Opera/9.68.(X11; Linux i686; mr-IN) Presto/2.9.185 Version/11.00"', '\n', '116.91.111.11 - - [21/Nov/2023:21:49:59 -0500] "PUT /wp-admin HTTP/1.0" 404 5067 "https://bailey.com/explore/mainlogin.html" "Opera/8.70.(X11; Linux i686; hak-TW) Presto/2.9.185 Version/12.00"', '\n', '191.241.91.254 - - [21/Nov/2023:21:51:05 -0500] "POST /wp-admin HTTP/1.0" 200 5002 "https://www.rowe-salazar.biz/categories/tagterms.html" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/26.0.823.0 Safari/532.0"', '\n', '210.162.29.112 - - [21/Nov/2023:21:52:09 -0500] "PUT /wp-admin HTTP/1.0" 200 5044 "https://chavez.com/blog/main/searchterms.jsp" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_1) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/57.0.810.0 Safari/533.2"', '\n', '218.23.241.187 - - [21/Nov/2023:21:55:01 -0500] "DELETE /wp-content HTTP/1.0" 200 5014 "http://www.porter.com/tags/main/mainterms.html" "Mozilla/5.0 (Windows NT 5.1; sat-IN; rv:1.9.0.20) Gecko/3167-11-18 23:43:25 Firefox/10.0"', '\n', '76.208.26.206 - - [21/Nov/2023:21:59:42 -0500] "GET /posts/posts/explore HTTP/1.0" 500 5030 "https://www.potts-houston.net/main/tagregister.html" "Mozilla/5.0 (Android 4.4.3; Mobile; rv:44.0) Gecko/44.0 Firefox/44.0"', '\n', '80.190.183.167 - - [21/Nov/2023:22:00:44 -0500] "GET /wp-admin HTTP/1.0" 200 5052 "https://www.cole.com/explore/tag/blogindex.html" "Opera/8.17.(X11; Linux x86_64; de-LI) Presto/2.9.161 Version/10.00"', '\n', '148.70.227.38 - - [21/Nov/2023:22:02:51 -0500] "GET /app/main/posts HTTP/1.0" 200 5049 "https://www.griffin.org/main/searchauthor.html" "Opera/9.86.(X11; Linux x86_64; iu-CA) Presto/2.9.169 Version/11.00"', '\n', '46.47.38.129 - - [21/Nov/2023:22:03:21 -0500] "DELETE /explore HTTP/1.0" 200 4973 "http://king.com/apphome.htm" "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.26.5 (KHTML, like Gecko) Version/5.0 Safari/535.26.5"', '\n', '13.30.23.86 - - [21/Nov/2023:22:04:40 -0500] "PUT /apps/cart.jsp?appID=6284 HTTP/1.0" 200 4991 "https://www.rowe.biz/tag/mainregister.html" "Mozilla/5.0 (Linux; Android 4.2) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/35.0.843.0 Safari/533.2"', '\n', '55.251.69.113 - - [21/Nov/2023:22:08:52 -0500] "PUT /explore HTTP/1.0" 200 4960 "http://www.lewis.com/tagsmain.html" "Mozilla/5.0 (Windows 95; shs-CA; rv:1.9.0.20) Gecko/9859-03-16 06:41:36 Firefox/4.0"', '\n', '146.127.169.31 - - [21/Nov/2023:22:13:22 -0500] "GET /list HTTP/1.0" 200 4947 "http://www.anderson.info/search/app/categoryabout.php" "Mozilla/5.0 (Linux; Android 4.4) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/19.0.803.0 Safari/532.1"', '\n', '168.100.255.243 - - [21/Nov/2023:22:14:02 -0500] "GET /wp-admin HTTP/1.0" 200 4999 "https://wood.com/list/categoriespost.php" "Mozilla/5.0 (Android 2.3.4; Mobile; rv:55.0) Gecko/55.0 Firefox/55.0"', '\n', '91.208.48.9 - - [21/Nov/2023:22:16:32 -0500] "POST /wp-admin HTTP/1.0" 200 4936 "https://www.harris-vaughn.com/tags/listlogin.htm" "Mozilla/5.0 (Windows NT 6.0; ia-FR; rv:1.9.0.20) Gecko/7347-03-04 19:45:42 Firefox/3.6.9"', '\n', '173.132.122.168 - - [21/Nov/2023:22:19:47 -0500] "GET /app/main/posts HTTP/1.0" 200 5040 "http://willis.com/main/appmain.asp" "Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1 like Mac OS X; be-BY) AppleWebKit/531.22.4 (KHTML, like Gecko) Version/3.0.5 Mobile/8B116 Safari/6531.22.4"', '\n', '25.107.30.44 - - [21/Nov/2023:22:23:27 -0500] "DELETE /wp-content HTTP/1.0" 200 4988 "http://barton-potts.com/main/searchabout.php" "Mozilla/5.0 (Android 5.0.2; Mobile; rv:26.0) Gecko/26.0 Firefox/26.0"', '\n', '157.108.123.38 - - [21/Nov/2023:22:26:35 -0500] "GET /app/main/posts HTTP/1.0" 200 5054 "http://www.beck-summers.info/search/postsprivacy.htm" "Mozilla/5.0 (Windows NT 5.2; tk-TM; rv:1.9.2.20) Gecko/7933-05-29 02:02:50 Firefox/3.8"', '\n', '166.151.58.145 - - [21/Nov/2023:22:30:59 -0500] "DELETE /wp-admin HTTP/1.0" 200 4990 "http://jones.com/category/categorieshome.htm" "Mozilla/5.0 (Windows NT 5.1; bs-BA; rv:1.9.0.20) Gecko/9878-05-27 14:43:25 Firefox/3.8"', '\n', '201.56.185.198 - - [21/Nov/2023:22:34:15 -0500] "PUT /app/main/posts HTTP/1.0" 200 5046 "http://vaughn.net/wp-content/wp-contentregister.asp" "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/534.2 (KHTML, like Gecko) FxiOS/18.8c4126.0 Mobile/86I335 Safari/534.2"', '\n', '101.96.9.187 - - [21/Nov/2023:22:35:38 -0500] "POST /search/tag/list HTTP/1.0" 301 4898 "https://sanders-patterson.info/explore/list/searchauthor.htm" "Mozilla/5.0 (Android 2.0; Mobile; rv:61.0) Gecko/61.0 Firefox/61.0"', '\n', '43.176.78.80 - - [21/Nov/2023:22:39:22 -0500] "DELETE /wp-admin HTTP/1.0" 200 4968 "http://www.edwards-wood.net/categories/searchmain.htm" "Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1 like Mac OS X; es-BO) AppleWebKit/533.3.7 (KHTML, like Gecko) Version/4.0.5 Mobile/8B113 Safari/6533.3.7"', '\n', '110.230.85.236 - - [21/Nov/2023:22:41:42 -0500] "GET /search/tag/list HTTP/1.0" 301 4954 "https://www.campbell.com/blog/taglogin.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.2 (KHTML, like Gecko) Chrome/41.0.883.0 Safari/536.2"', '\n', '49.244.193.159 - - [21/Nov/2023:22:43:22 -0500] "GET /wp-content HTTP/1.0" 200 5003 "https://www.valdez.com/blog/category/blogpost.php" "Mozilla/5.0 (Android 3.2.1; Mobile; rv:37.0) Gecko/37.0 Firefox/37.0"', '\n', '25.243.127.208 - - [21/Nov/2023:22:44:25 -0500] "GET /app/main/posts HTTP/1.0" 200 4957 "http://www.marquez-nicholson.com/mainpost.html" "Mozilla/5.0 (iPad; CPU iPad OS 10_3_4 like Mac OS X) AppleWebKit/532.1 (KHTML, like Gecko) FxiOS/18.6y6157.0 Mobile/39L406 Safari/532.1"', '\n', '134.82.4.25 - - [21/Nov/2023:22:46:32 -0500] "POST /search/tag/list HTTP/1.0" 200 4948 "https://montoya.com/list/mainlogin.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0; rv:1.9.5.20) Gecko/4956-11-29 03:03:57 Firefox/3.6.20"', '\n', '25.148.90.54 - - [21/Nov/2023:22:48:32 -0500] "PUT /search/tag/list HTTP/1.0" 404 4943 "http://www.grant.com/wp-content/posts/listsearch.asp" "Mozilla/5.0 (Linux; Android 4.0.1) AppleWebKit/535.0 (KHTML, like Gecko) Chrome/14.0.804.0 Safari/535.0"', '\n', '37.147.56.205 - - [21/Nov/2023:22:53:00 -0500] "GET /posts/posts/explore HTTP/1.0" 200 5097 "https://jefferson.com/category/search/tagsearch.php" "Mozilla/5.0 (Linux; Android 1.0) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/37.0.865.0 Safari/533.0"', '\n', '204.241.197.151 - - [21/Nov/2023:22:56:08 -0500] "PUT /wp-content HTTP/1.0" 200 5083 "https://www.moran-reyes.com/wp-content/exploreregister.asp" "Mozilla/5.0 (Linux; Android 9) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/17.0.830.0 Safari/534.1"', '\n', '215.17.31.88 - - [21/Nov/2023:22:59:52 -0500] "GET /wp-admin HTTP/1.0" 200 4944 "https://valdez.com/categoriesterms.html" "Mozilla/5.0 (Windows NT 6.1; sk-SK; rv:1.9.1.20) Gecko/6967-01-06 16:32:43 Firefox/9.0"', '\n', '142.172.26.1 - - [21/Nov/2023:23:01:43 -0500] "GET /posts/posts/explore HTTP/1.0" 200 4919 "http://mccarty.com/tagpost.htm" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_1; rv:1.9.5.20) Gecko/9602-08-05 17:35:22 Firefox/3.6.17"', '\n', '58.39.51.211 - - [21/Nov/2023:23:03:39 -0500] "POST /apps/cart.jsp?appID=3056 HTTP/1.0" 200 5018 "http://sparks-jones.net/app/postscategory.htm" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/25.0.893.0 Safari/534.0"', '\n', '24.133.43.120 - - [21/Nov/2023:23:06:33 -0500] "PUT /posts/posts/explore HTTP/1.0" 200 4993 "http://www.olson.biz/listcategory.htm" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2; rv:1.9.6.20) Gecko/9447-11-05 15:17:46 Firefox/7.0"', '\n', '42.232.210.81 - - [21/Nov/2023:23:10:11 -0500] "GET /posts/posts/explore HTTP/1.0" 200 5056 "http://www.hoover.com/listhomepage.jsp" "Opera/8.28.(Windows 95; uk-UA) Presto/2.9.182 Version/12.00"', '\n', '43.30.2.191 - - [21/Nov/2023:23:11:25 -0500] "GET /apps/cart.jsp?appID=5093 HTTP/1.0" 200 4969 "https://marshall.com/tagfaq.html" "Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/2953-06-11 01:59:42 Firefox/4.0"', '\n', '159.231.99.146 - - [21/Nov/2023:23:13:44 -0500] "PUT /posts/posts/explore HTTP/1.0" 200 4949 "http://fisher-hughes.biz/wp-content/postsabout.php" "Mozilla/5.0 (Android 4.0.3; Mobile; rv:67.0) Gecko/67.0 Firefox/67.0"', '\n', '106.170.103.125 - - [21/Nov/2023:23:16:51 -0500] "GET /explore HTTP/1.0" 200 4953 "https://gonzalez.com/blog/wp-content/postsmain.php" "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_6 like Mac OS X) AppleWebKit/535.2 (KHTML, like Gecko) CriOS/60.0.869.0 Mobile/62S841 Safari/535.2"', '\n', '126.161.171.85 - - [21/Nov/2023:23:19:49 -0500] "GET /apps/cart.jsp?appID=6910 HTTP/1.0" 200 5011 "http://www.jones-stewart.com/posts/tag/listregister.php" "Mozilla/5.0 (Android 2.3.3; Mobile; rv:10.0) Gecko/10.0 Firefox/10.0"', '\n', '21.115.65.215 - - [21/Nov/2023:23:21:18 -0500] "GET /list HTTP/1.0" 200 5049 "https://walker.com/blogfaq.php" "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0)"', '\n', '118.23.9.233 - - [21/Nov/2023:23:24:08 -0500] "PUT /app/main/posts HTTP/1.0" 200 4981 "http://www.shannon.com/search/list/categoryhomepage.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/22.0.875.0 Safari/534.2"', '\n', '17.38.144.31 - - [21/Nov/2023:23:28:35 -0500] "GET /wp-content HTTP/1.0" 200 4913 "http://molina.com/posts/listsearch.htm" "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Trident/4.0)"', '\n', '179.133.77.41 - - [21/Nov/2023:23:31:51 -0500] "GET /app/main/posts HTTP/1.0" 200 5048 "https://lowe.com/tags/tag/tagsfaq.html" "Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/9535-02-20 03:44:24 Firefox/3.6.2"', '\n', '12.194.145.77 - - [21/Nov/2023:23:34:09 -0500] "DELETE /apps/cart.jsp?appID=2627 HTTP/1.0" 200 4971 "https://mccoy-king.com/tags/listmain.php" "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_10_9; rv:1.9.5.20) Gecko/3366-04-19 22:24:49 Firefox/12.0"', '\n', '165.131.153.87 - - [21/Nov/2023:23:37:06 -0500] "POST /app/main/posts HTTP/1.0" 200 5031 "http://ortiz.biz/mainregister.html" "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_7; rv:1.9.5.20) Gecko/7642-07-31 05:28:11 Firefox/3.6.18"', '\n', '129.31.168.88 - - [21/Nov/2023:23:37:49 -0500] "GET /app/main/posts HTTP/1.0" 200 5005 "http://www.jones.com/tag/wp-contentsearch.html" "Mozilla/5.0 (Linux; Android 4.4.1) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/51.0.825.0 Safari/531.2"', '\n', '120.227.51.119 - - [21/Nov/2023:23:39:43 -0500] "DELETE /wp-admin HTTP/1.0" 200 5043 "http://chambers.org/categories/posts/postsindex.html" "Mozilla/5.0 (Linux; Android 2.2.2) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/59.0.831.0 Safari/533.2"', '\n', '217.2.187.49 - - [21/Nov/2023:23:42:40 -0500] "PUT /app/main/posts HTTP/1.0" 200 5071 "https://www.carey.com/categories/wp-content/exploreindex.html" "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.6.20) Gecko/4522-09-12 22:47:43 Firefox/3.8"', '\n', '197.120.138.142 - - [21/Nov/2023:23:44:39 -0500] "GET /wp-admin HTTP/1.0" 200 4988 "http://bowers.net/tagsindex.html" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_7; rv:1.9.4.20) Gecko/7427-08-27 20:15:50 Firefox/3.8"', '\n', '100.227.252.167 - - [21/Nov/2023:23:47:20 -0500] "GET /explore HTTP/1.0" 200 4989 "http://www.lane.org/app/tagsearch.htm" "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_10_1; rv:1.9.2.20) Gecko/3417-02-08 23:48:52 Firefox/3.8"', '\n', '185.54.38.47 - - [21/Nov/2023:23:48:58 -0500] "GET /wp-admin HTTP/1.0" 200 4922 "http://obrien-suarez.com/mainmain.htm" "Mozilla/5.0 (Windows NT 4.0; el-CY; rv:1.9.1.20) Gecko/9393-08-15 03:32:11 Firefox/3.6.16"', '\n', '119.219.73.14 - - [21/Nov/2023:23:50:09 -0500] "POST /list HTTP/1.0" 200 4965 "https://olson.net/wp-content/list/categorieshomepage.html" "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/6819-07-07 22:22:55 Firefox/12.0"', '\n', '72.24.25.223 - - [21/Nov/2023:23:52:28 -0500] "GET /wp-content HTTP/1.0" 200 5086 "https://nguyen.com/categorieslogin.php" "Mozilla/5.0 (Linux; Android 4.0.3) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/41.0.870.0 Safari/534.2"', '\n', '169.96.9.132 - - [21/Nov/2023:23:53:40 -0500] "GET /search/tag/list HTTP/1.0" 200 4931 "http://robinson.com/searchauthor.html" "Mozilla/5.0 (Windows NT 6.2; tk-TM; rv:1.9.0.20) Gecko/7505-04-23 08:30:04 Firefox/3.6.17"', '\n', '65.20.23.60 - - [21/Nov/2023:23:58:39 -0500] "GET /apps/cart.jsp?appID=1604 HTTP/1.0" 200 4990 "http://hill-francis.com/blog/posts/postssearch.php" "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/26.0.890.0 Safari/534.0"', '\n', '134.51.18.248 - - [22/Nov/2023:00:02:48 -0500] "GET /app/main/posts HTTP/1.0" 301 5014 "https://flores.com/posts/category/bloghomepage.asp" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/61.0.804.0 Safari/533.0"', '\n', '35.149.1.134 - - [22/Nov/2023:00:04:10 -0500] "POST /apps/cart.jsp?appID=4646 HTTP/1.0" 200 5031 "http://smith.com/listlogin.php" "Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.1; Trident/5.0)"', '\n', '117.5.22.249 - - [22/Nov/2023:00:04:47 -0500] "GET /search/tag/list HTTP/1.0" 200 5076 "https://www.garcia.org/tag/listauthor.asp" "Mozilla/5.0 (X11; Linux i686; rv:1.9.6.20) Gecko/3948-04-20 10:11:59 Firefox/15.0"', '\n', '194.115.179.226 - - [22/Nov/2023:00:08:24 -0500] "GET /wp-admin HTTP/1.0" 200 5004 "http://www.ruiz.com/tag/tagscategory.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_1) AppleWebKit/536.2 (KHTML, like Gecko) Chrome/40.0.832.0 Safari/536.2"', '\n', '185.3.38.175 - - [22/Nov/2023:00:09:48 -0500] "DELETE /wp-admin HTTP/1.0" 200 4993 "https://compton.com/category/category/exploreauthor.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8 rv:6.0; ka-GE) AppleWebKit/535.4.1 (KHTML, like Gecko) Version/4.1 Safari/535.4.1"', '\n', '8.124.142.48 - - [22/Nov/2023:00:13:37 -0500] "DELETE /posts/posts/explore HTTP/1.0" 200 5056 "https://www.brown.com/exploreregister.htm" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_1; rv:1.9.3.20) Gecko/6068-10-31 08:05:42 Firefox/3.6.4"', '\n', '9.36.14.199 - - [22/Nov/2023:00:15:10 -0500] "GET /explore HTTP/1.0" 200 4925 "http://www.mann.com/appfaq.php" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_4 rv:5.0; pap-CW) AppleWebKit/533.21.3 (KHTML, like Gecko) Version/4.1 Safari/533.21.3"', '\n', '161.142.120.77 - - [22/Nov/2023:00:17:05 -0500] "GET /apps/cart.jsp?appID=3979 HTTP/1.0" 200 5026 "https://greene-daniels.net/tags/appfaq.html" "Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gecko/4347-09-20 03:16:23 Firefox/13.0"', '\n', '189.233.93.103 - - [22/Nov/2023:00:20:16 -0500] "GET /posts/posts/explore HTTP/1.0" 200 4928 "https://cross.com/blogsearch.jsp" "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/533.2 (KHTML, like Gecko) CriOS/26.0.852.0 Mobile/69D756 Safari/533.2"', '\n', '163.231.214.155 - - [22/Nov/2023:00:22:01 -0500] "DELETE /app/main/posts HTTP/1.0" 200 5066 "https://green.com/tagsabout.htm" "Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/4746-12-03 18:45:48 Firefox/3.8"', '\n', '16.36.87.129 - - [22/Nov/2023:00:22:56 -0500] "GET /explore HTTP/1.0" 500 5066 "https://thomas.com/list/list/categoryauthor.html" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_4) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/51.0.867.0 Safari/531.2"', '\n', '42.219.124.190 - - [22/Nov/2023:00:26:45 -0500] "PUT /search/tag/list HTTP/1.0" 200 5017 "http://barker.info/mainabout.html" "Mozilla/5.0 (iPad; CPU iPad OS 5_1_1 like Mac OS X) AppleWebKit/532.0 (KHTML, like Gecko) FxiOS/11.3i5428.0 Mobile/37B401 Safari/532.0"', '\n', '214.117.145.63 - - [22/Nov/2023:00:28:14 -0500] "GET /apps/cart.jsp?appID=4005 HTTP/1.0" 200 4956 "http://kennedy.net/listprivacy.html" "Mozilla/5.0 (Android 6.0.1; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0"', '\n', '49.80.198.131 - - [22/Nov/2023:00:29:05 -0500] "GET /explore HTTP/1.0" 200 4889 "https://sanchez-perez.com/wp-contenthome.asp" "Mozilla/5.0 (Windows; U; Windows NT 10.0) AppleWebKit/531.13.2 (KHTML, like Gecko) Version/5.0.3 Safari/531.13.2"', '\n', '68.84.25.203 - - [22/Nov/2023:00:30:03 -0500] "PUT /app/main/posts HTTP/1.0" 200 5034 "https://gomez-west.com/listabout.htm" "Mozilla/5.0 (Windows CE) AppleWebKit/535.0 (KHTML, like Gecko) Chrome/62.0.857.0 Safari/535.0"', '\n', '193.229.123.152 - - [22/Nov/2023:00:34:30 -0500] "GET /explore HTTP/1.0" 200 5043 "http://www.hill.com/postscategory.htm" "Mozilla/5.0 (X11; Linux i686; rv:1.9.6.20) Gecko/8675-12-07 11:16:26 Firefox/5.0"', '\n', '133.211.151.84 - - [22/Nov/2023:00:38:29 -0500] "GET /explore HTTP/1.0" 200 4995 "http://kidd.org/wp-contentauthor.php" "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.1)"', '\n', '185.246.187.62 - - [22/Nov/2023:00:40:09 -0500] "GET /wp-admin HTTP/1.0" 200 5001 "http://www.barnett-hodges.info/blog/blogcategory.php" "Mozilla/5.0 (Android 2.2; Mobile; rv:65.0) Gecko/65.0 Firefox/65.0"', '\n', '105.85.169.49 - - [22/Nov/2023:00:42:41 -0500] "GET /apps/cart.jsp?appID=4813 HTTP/1.0" 200 5099 "https://pitts.org/tagregister.php" "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_11_2) AppleWebKit/531.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/531.1"', '\n', '201.36.89.39 - - [22/Nov/2023:00:45:49 -0500] "GET /search/tag/list HTTP/1.0" 200 5039 "http://www.davis.com/wp-content/blogregister.php" "Mozilla/5.0 (Windows; U; Windows NT 4.0) AppleWebKit/531.39.2 (KHTML, like Gecko) Version/5.0.5 Safari/531.39.2"', '\n', '193.111.17.198 - - [22/Nov/2023:00:47:58 -0500] "GET /explore HTTP/1.0" 200 4983 "http://jensen-yang.org/wp-content/search/bloglogin.jsp" "Mozilla/5.0 (Android 6.0.1; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0"', '\n', '197.240.94.39 - - [22/Nov/2023:00:48:38 -0500] "DELETE /wp-admin HTTP/1.0" 200 4966 "http://www.kirk.biz/tag/category/searchterms.php" "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/6430-08-06 10:09:00 Firefox/3.6.20"', '\n', '114.120.178.140 - - [22/Nov/2023:00:52:18 -0500] "GET /posts/posts/explore HTTP/1.0" 200 4874 "https://www.randolph.biz/categorysearch.html" "Mozilla/5.0 (Android 7.1.2; Mobile; rv:7.0) Gecko/7.0 Firefox/7.0"', '\n', '28.223.225.137 - - [22/Nov/2023:00:52:50 -0500] "GET /search/tag/list HTTP/1.0" 200 4975 "http://boone.org/wp-content/wp-contentmain.asp" "Mozilla/5.0 (iPad; CPU iPad OS 5_1_1 like Mac OS X) AppleWebKit/531.2 (KHTML, like Gecko) FxiOS/14.8k9632.0 Mobile/17L234 Safari/531.2"', '\n', '18.84.52.224 - - [22/Nov/2023:00:56:10 -0500] "GET /wp-admin HTTP/1.0" 200 4929 "https://www.gallagher.info/main/tag/wp-contentlogin.asp" "Mozilla/5.0 (Linux; Android 4.1.2) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/53.0.846.0 Safari/531.0"', '\n', '60.114.184.47 - - [22/Nov/2023:00:58:27 -0500] "GET /wp-admin HTTP/1.0" 404 4979 "https://ward-frazier.com/category/appmain.html" "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.6.20) Gecko/9248-08-25 23:26:16 Firefox/3.8"', '\n', '122.254.239.138 - - [22/Nov/2023:01:02:50 -0500] "PUT /app/main/posts HTTP/1.0" 200 5071 "http://shields.com/explore/blogfaq.htm" "Mozilla/5.0 (iPad; CPU iPad OS 7_1_2 like Mac OS X) AppleWebKit/532.2 (KHTML, like Gecko) FxiOS/14.1b6694.0 Mobile/88Q626 Safari/532.2"', '\n', '57.245.29.50 - - [22/Nov/2023:01:05:10 -0500] "POST /search/tag/list HTTP/1.0" 200 5040 "https://williams.net/tags/categorysearch.htm" "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3 like Mac OS X; sa-IN) AppleWebKit/532.15.6 (KHTML, like Gecko) Version/3.0.5 Mobile/8B114 Safari/6532.15.6"', '\n', '145.201.205.36 - - [22/Nov/2023:01:08:29 -0500] "GET /wp-admin HTTP/1.0" 200 5005 "https://www.tyler.com/posts/tag/categoryfaq.php" "Mozilla/5.0 (Android 2.2.3; Mobile; rv:8.0) Gecko/8.0 Firefox/8.0"', '\n', '28.113.143.13 - - [22/Nov/2023:01:10:12 -0500] "GET /wp-content HTTP/1.0" 200 4932 "http://www.rodriguez-bailey.com/searchpost.htm" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_0; rv:1.9.5.20) Gecko/2444-02-01 09:55:11 Firefox/3.8"', '\n', '6.112.222.16 - - [22/Nov/2023:01:13:36 -0500] "GET /app/main/posts HTTP/1.0" 301 4975 "https://www.anthony.info/tags/main/listindex.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/535.0 (KHTML, like Gecko) FxiOS/14.8x0255.0 Mobile/41U734 Safari/535.0"', '\n', '207.74.255.152 - - [22/Nov/2023:01:15:22 -0500] "PUT /wp-content HTTP/1.0" 200 4929 "http://www.harvey.biz/tags/taglogin.htm" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8; rv:1.9.3.20) Gecko/2937-12-10 03:24:59 Firefox/3.8"', '\n', '156.228.44.5 - - [22/Nov/2023:01:19:29 -0500] "GET /search/tag/list HTTP/1.0" 200 4905 "http://francis.com/categories/search/postsabout.php" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_6) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/15.0.834.0 Safari/531.2"', '\n', '184.89.199.78 - - [22/Nov/2023:01:20:05 -0500] "GET /posts/posts/explore HTTP/1.0" 200 4929 "http://drake.com/posts/tagsearch.html" "Mozilla/5.0 (Android 4.3; Mobile; rv:6.0) Gecko/6.0 Firefox/6.0"', '\n', '13.125.239.110 - - [22/Nov/2023:01:21:41 -0500] "DELETE /apps/cart.jsp?appID=4550 HTTP/1.0" 200 5078 "https://www.russell-gallegos.com/wp-contentsearch.html" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/34.0.817.0 Safari/533.0"', '\n', '55.151.65.6 - - [22/Nov/2023:01:25:16 -0500] "GET /app/main/posts HTTP/1.0" 200 5088 "https://conley-douglas.net/mainregister.htm" "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/534.1 (KHTML, like Gecko) FxiOS/17.1c2265.0 Mobile/75A255 Safari/534.1"', '\n', '185.54.69.221 - - [22/Nov/2023:01:27:20 -0500] "PUT /apps/cart.jsp?appID=4258 HTTP/1.0" 200 5111 "http://manning-obrien.com/blog/categoriesmain.htm" "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_1 like Mac OS X; lo-LA) AppleWebKit/534.6.7 (KHTML, like Gecko) Version/3.0.5 Mobile/8B115 Safari/6534.6.7"', '\n', '']
color=Fore.GREEN
version=input(f"{color}Which version would you like to install(press enter for latest)(type 'update' to update): ")
if version == "update":
    os.system("cls")
    update_version=input("Input update version: ")
    if update_version=="2.1":
        os.system("cls")
        print("Find 'install_v2_1' in the code to update")
        print("Just replace the string with the new string(copied and pasted from the updater)")
    elif update_version=="2.0":
        os.system("cls")
        print("Find 'install_v2_0' in the code to update")
        print("Just replace the string with the new string(copied and pasted from the updater)")
    elif update_version=="1.0":
        os.system("cls")
        print("Find 'install_v1_0' in the code to update")
        print("Just replace the string with the new string(copied and pasted from the updater)")
    input()
    os.system("cls")
    exit()
    
os.system("cls")
log=input("Would you like a detailed log(press enter if no)(if yes type 'yes'): ")
os.system("cls")
path=input("Input file path(do not include file name only the folder): ")
os.system("cls")
inject=input("Would you like to directly inject the library to a certain file(press enter if no)(type 'yes' if yes): ")
if not inject == "":
    os.system("cls")
    inject=input(f"{color}Input path for injection{color2}(INCLUDE FILE NAME):{color} ")
    if ":" in inject:
        with open(inject, "r") as og:
            if not "from py_logger import *" in og.read():
                with open(inject, 'r') as original:
                   data = original.read()
                with open(inject, 'w') as modified:
                    modified.write("from py_logger import *\n" + data)
    else:
        os.system("cls")
        print(f"{color2}⚠ ERROR: Could not find path")
        exit()
os.system("cls")
versionnum=f"{path}\py_logger.py"
versionid=f"install_v{version}"
if version=="":
    version="2.1"
    versionid=f"install_v{version}"
    with open(versionnum, "w") as install:
        install.write(install_v2_1)
    if log=="yes":
        for i in logging:
            print(i)
        for i in range(10):
            t=10-i
            if t==1:
                os.system("cls")
            else:
                print(f"Clearing log in {t} seconds...")
            time.sleep(1.0)
    else:
        load("2.1")
elif version=="2.0":
    with open(versionnum, "w") as install:
        install.write(install_v2_0)
    if log=="yes":
        for i in logging:
            print(i)
        for i in range(10):
            t=10-i
            print(f"Clearing log in {t} seconds...")
            time.sleep(1.0)
    else:
        load("2.0")
elif version=="1.0":
    with open(versionnum, "w") as install:
        install.write(install_v1_0)
    if log=="yes":
        for i in logging:
            print(i)
        for i in range(10):
            t=10-i
            print(f"Clearing log in {t} seconds...")
            time.sleep(1.0)
    else:
        load("1.0")
