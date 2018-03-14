init:
    python:

        connections={     "home":["city"],
                          "city":["home","mountain","market"],
                      "mountain":["city","observatory","beach"],
                        "market":["city"],
                   "observatory":["mountain"],
                         "beach":["mountain"]}
        weekdays = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
        times = ("dawn","noon","dusk","midnight")


        class thing():
            def __init__(self, name="???", description="This item doesn't exist.", image="exitbutton_hover.png", action=None):
                self.name=name
                self.description=description
                self.image=image
                self.action=action
                pass


        #item declarations go down here
        blue_key=thing(name="Blue key", description="Just a regular key.", image="key_%s.png", action="item_city")
    image bg black = "#000"

default backpack_items = []
default currplace= "home"
default clockint = 3
default clockstr = ""
default dateint  =-1
default datestr  = ""
default displaytime=""



label time_advance():
    python:
        clockint+=1                             #advance the time
        if clockint >=4:                        #carry over
            clockint=0
            dateint = dateint+1
        dateWeekModulo = dateint%7              #set display text
        datestr = weekdays[dateWeekModulo]
        clockstr= times[clockint]
        displaytime = "it's "+datestr+" at "+clockstr+"."
    return





label start:
    jump home
label mnlp:
    python:     #BUILDING THE MENU
        menulist=[]
        for i in connections[currplace]:
            menulist.append((i,i)) #TODO change it so locations have pretty names?
        currjump=renpy.display_menu(menulist,screen="backpack")
        if currjump[:5]=="item_":
            pass #TODO You sit down and take [item] out...
        else:
            currplace=currjump
    #test code
    "[currplace]"
    jump mnlp
    #end test code

    scene bg black with dissolve
    call time_advance
    scene timebg:
        zoom 1280 #TODO fix so that the colors represent the time
    show expression "bg "+currplace as bg
    with dissolve
    $renpy.jump(currplace)
    return

label home:
