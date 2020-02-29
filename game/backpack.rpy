default backpack_list = []


init:
    python:
        class item():
            def __init__(self, name="???", description="This item doesn't exist.", image="exitbutton_hover.png", action=None):
                self.name=name                  #the name that will be displayed
                self.description=description    #description shown on hover
                self.image=image                #the image for the file - currently disabled as of 2020-02-29
                self.action=action              #the label to be called when the user clicks on the item
                pass

screen backpack( items=[["hola",NullAction()]] ):
    tag menu
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
                ## this piece of code is to use the backpack menu as a replacement for the location menu
                ## as of 2020-02-29 I'm  using a separate location menu (see exploration.rpy) so it's commented out
                # frame:
                #     xfill True
                #     text "Go somewhere..."
                # vpgrid:
                #     cols 2
                #     for i in items:
                #         frame:
                #             xysize (294,50)
                #             textbutton i.caption action i.action:
                #                 tooltip "Go to the "+i.caption+"."
                #                 yalign 0.5
                #
                # null height 20
                ## end of this piece of code to replace the backpack menu
                frame:
                    xfill True
                    text "Use an item."
                vpgrid:
                    cols 2
                    frame:
                        xysize (294,50)
                        textbutton "Go back." action Return("back"):
                            tooltip "Return to the previous screen."
                            yalign 0.5
                    for i in backpack_list:
                        frame:
                            xysize (294,50)
                            textbutton i.name action Return(i.action):
                                tooltip i.description
                                yalign 0.5
                        ##kinda sad that this image arg is unused - I'm hoping to add it in a future release of the game tho. 
                        ##
                        # imagebutton auto i.image action Return(i.action):
                        #     tooltip i.description
        frame:
            padding (10,10)
            $tooltip=GetTooltip()
            xysize (600,100)
            if tooltip:
                text "[tooltip]"
            else:
                text "Hover an item to know more."


screen stats_screen: #this is for the stats at the top left corner i think. im a little bit drunk
                        #this is also referenced at the top of screens.rpy for some ungodly reason.2020-02-29
    zorder 100
    style_prefix "stats"
    if show_stats:
        vbox:
            xalign 1.0
            yalign 0.0
            python:
                if len(backpack_list) == 1: #TODO make modular so I can put weird stuff
                                            #what the fuck did i mean by that
                                            # wtf did i mean by wtf. i gotta start uptting timestamps on my comment.s 2020-02-29
                    ui.text("there is 1 item in your backpack.")
                else:
                    ui.text("there are "+str(len(backpack_list))+" items in your backpack.")
            if displaytime:
                text "[displaytime] [clockint]" xalign 1.0
