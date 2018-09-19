default weekdays = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
default times = ("dawn","noon","dusk","midnight")
default clockint = 3
default clockstr = ""
default dateint  =-1
default datestr  = ""
default displaytime=""

label time_advance():
    python:
        clockint+=1                                 #advance the time
        if clockint >=4:                            #carry over
            clockint=0
            dateint = dateint+1
        dateWeekModulo = dateint%7                  #set display text
        datestr = weekdays[dateWeekModulo]
        clockstr= times[clockint]
        displaytime = "it's "+datestr+" at "+clockstr+"."
    return
