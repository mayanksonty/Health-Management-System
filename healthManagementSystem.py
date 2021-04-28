logOrRetrive = int(input("Want to log or Retrive 1 for log 2 for retrive"))


def log (name,exOrDiet,logVal):
    if exOrDiet == 1:
        if name == 1:
            with open("harryExer.txt","a") as f:
                f.write(logVal)
        elif name == 2:
            with open("rohanExer.txt","a") as f:
                f.write(logVal)
        elif name == 3:
            with open("ShubhamExer.txt","a") as f:
                f.write(logVal)
    elif exOrDiet == 2:
        if name == 1:
            with open("harryDiet.txt","a") as f:
                f.write(logVal)
        elif name == 2:
            with open("rohanDiet.txt","a") as f:
                f.write(logVal)
        elif name == 3:
            with open("ShubhamDiet.txt","a") as f:
                f.write(logVal)

def getdate():
    import datetime
    return datetime.datetime.now()


def retrive(name):
    with open(name) as f:
        for line in f:
            print(line, end="")


i = 1
while(i == 1):
    d = str(getdate())
    if logOrRetrive == 1:
        exOrDiet = int(input("Want to log for 1 = Excersise or 2 = Diet "))
        name = int(input("Log for 1 = harry, 2 = rohan, 3 = shubham"))
        value = input("Enter the things")
        logValue = "["+d+"]"+" "+value+"\n"
        log(name,exOrDiet,logValue)
    elif logOrRetrive == 2:
        exOrDiet = int(input("Want to log for 1 = Excersise or 2 = Diet "))
        value = int(input("hit 1 for Harry, 2 for rohan, 3 for shubham") )
        if exOrDiet == 1:
            if value == 1:
                retrive("harryExer.txt")
            elif value == 2:
                retrive("rohanExer.txt")
            elif value == 3:
                retrive("shubhamExer.txt")
        elif exOrDiet == 2:
            if value == 1:
                retrive("harryDiet.txt")
            elif value == 2:
                retrive("rohanDiet.txt")
            elif value == 3:
                retrive("shubhamDiet.txt")
    i = int(input("for exit 1 for continue 2"))

