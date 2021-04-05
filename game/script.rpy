init:
    python:
        #item declarations go down here
        blue_key=item( name="Blue key",
                        description="Just a regular key.",
                        image="key_%s.png",
                        action="key")
        music_player=item( name="music player",
                            description="A portable music player.",
                            image="key_%s.png",
                            action="music_player")
    image black = "#000"

default location_names = {  "home":"workshop",
                            "city":"crossroads",
                            "labo":"computer laboratory",
                            "track":"gymnasium",
                            "astro":"astronomical observatory"}

default events = {  "home":None,
                    "city":None,
                    "labo":None,
                    "track":None,
                    "astro":None}

default currplace= "home"
default listeningToMusicPlayer = False
default connections={     "home":["city"],
                          "city":["home","labo","track","astro"],
                          "labo":["city"],
                          "track":["city"],
                          "astro":["city"]}

label bgshow(advance=False): #TODO add a place argument
    scene black with dissolve
    python:
        #I'm using these variables because it works funky if i put the expression in the same line. 
        timeColorTransitionStart=float(clockint)/4
        timeColorTransitionEnd=float(clockint+1)/4
    show timebg:
        xalign timeColorTransitionStart#(float(clockint)/4)
        zoom 1280 #TODO fix so that the colors represent the time
    if advance:
        call time_advance
        if clockint==0: #reset to the start of the long strip if we're at the end already, otherwise just advance
            show timebg:
                linear 1.0 xalign timeColorTransitionEnd#(float(clockint+1)/4) 
                xalign 0.0
        else:
            show timebg:
                linear 1.0 xalign timeColorTransitionEnd#(float(clockint+1)/4) 
    show expression "bg "+currplace as bg
    with dissolve
    return


define b = Character("{color=#f00}blessed{/color}")
define h = Character("{color=#0f0}hexed{/color}")
define c = Character("{color=#00f}charmed{/color}")
define s = Character("{color=#fff}strange{/color}")




label start:
    $currplace="labo"
    $events["astro"]="blessed_blueprints"
    $events["home"]="strange_blueprints"
    $events["track"]="charmed_blueprints"


    call bgshow(advance=True)

    "Tick."
    "The gears on the desk spin one step forwards."
    s "Hmmm..."
    s "Does that look right?"
    h "I think that looks right."
    s "Let's try another step."
    "Tock."
    "Another step."
    s "Looking good so far, isn't it?"
    h "Yeah, that's probably, like, exciting, or something."
    h "Maybe you should try running it on auto for a while."
    "With the flick of a switch, I start running it."
    "Tick-tock. Tick-tock."

    ##TODO: add an option to "head back inside" or to repeat the current event?)


    jump mainloop #in exploration.rpy




label key:
    "you have a super secret key"
    return
label music_player:
    if listeningToMusicPlayer:
        "you took the music player off"
        $ listeningToMusicPlayer = False
    else:
        $ listeningToMusicPlayer = True
        "you put on the music player"
        "dun durun dun dun"
        "you just heard some music"
    return
