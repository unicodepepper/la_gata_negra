default weekdays = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
default times = ("dawn","noon","dusk","midnight")
default backpack_items = []
default currplace= "home"
default clockint = 3
default clockstr = ""
default dateint  =-1
default datestr  = ""
default displaytime=""
default connections={     "home":["city"],
                          "city":["home"]}

init:
    python:
        class thing():
            def __init__(self, name="???", description="This item doesn't exist.", image="exitbutton_hover.png", action=None):
                self.name=name
                self.description=description
                self.image=image
                self.action=action
                pass

screen backpack(items=[["hola",NullAction()]]):
    vbox:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 600
        xfill True
        yfill True
        vpgrid:
            ymaximum 400
            yminimum 400
            cols 1
            #spacing 5
            draggable True
            mousewheel True
            scrollbars "vertical"

            # Since we have scrollbars, we have to position the side, rather
            # than the vpgrid proper.
            #side_xalign 0.5
            vbox:
                frame:
                    xfill True
                    text "Go somewhere..."
                vpgrid:
                    cols 2
                    for i in items:
                        frame:
                            xysize (294,50)
                            textbutton i.caption action i.action:
                                tooltip "Go to the "+i.caption+"."
                                yalign 0.5

                null height 20

                frame:
                    xfill True
                    text "...or use an item."
                vpgrid:
                    cols 2
                    for i in backpack_items:
                        # frame:
                        #     xysize (294,50)
                        #     textbutton i.name action Return(i.action):
                        #         tooltip i.description
                        #         yalign 0.5
                        imagebutton auto i.image action Return(i.action):
                            tooltip i.description
        frame:
            padding (10,10)
            $tooltip=GetTooltip()
            xysize (600,100)
            if tooltip:
                text "[tooltip]"

screen stats_screen:
    zorder 100
    style_prefix "stats"
    if show_stats:
        vbox:
            xalign 1.0
            yalign 0.0
            if displaytime:
                text "[displaytime]" xalign 1.0
            python:
                if len(backpack_items) == 1: #TODO make modular so I can put weird stuff
                    ui.text("there is 1 item in your backpack.")
                else:
                    ui.text("there are "+str(len(backpack_items))+" items in your backpack.")

label mainloop:
    python:     #BUILDING THE MENU
        menulist=[]
        for i in connections[currplace]:
            menulist.append((i,i)) #TODO change it so locations have pretty names?
        currjump=renpy.display_menu(menulist,screen="backpack")
        if currjump[:5]=="item_":
            pass #TODO You sit down and take [item] out...
        else:
            currplace=currjump
    scene bg black with dissolve
    call time_advance
    scene timebg:
        zoom 1280 #TODO fix so that the colors represent the time
    show expression "bg "+currplace as bg
    with dissolve
    $renpy.jump(currplace)
    return

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
