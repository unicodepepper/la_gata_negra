init:
    python:
        #item declarations go down here
        blue_key=thing(name="Blue key", description="Just a regular key.", image="key_%s.png", action="key")
    image bg black = "#000"


default currplace= "home"
default connections={     "home":["city"],
                          "city":["home"]}


label bgshow:
    scene bg black with dissolve
    call time_advance
    scene timebg:
        zoom 1280 #TODO fix so that the colors represent the time
    show expression "bg "+currplace as bg
    with dissolve
    return

label start:
    call bgshow
    jump mainloop

label home:
    $currplace="home"
    call bgshow
    "klok"
    return

label city:
    $currplace="city"
    call bgshow
    "dime ab"
    return


label key:
    "you have a super secret key"
    return
