default backpack_list = []


init:
    python:
        class thing():
            def __init__(self, name="???", description="This item doesn't exist.", image="exitbutton_hover.png", action=None):
                self.name=name
                self.description=description
                self.image=image
                self.action=action
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
                        # imagebutton auto i.image action Return(i.action):
                        #     tooltip i.description
        frame:
            padding (10,10)
            $tooltip=GetTooltip()
            xysize (600,100)
            if tooltip:
                text "[tooltip]"
            else:
                text "sorry for the shitty icon, it's all i've made"
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
                if len(backpack_list) == 1: #TODO make modular so I can put weird stuff
                                            #what the fuck did i mean by that
                    ui.text("there is 1 item in your backpack.")
                else:
                    ui.text("there are "+str(len(backpack_list))+" items in your backpack.")
