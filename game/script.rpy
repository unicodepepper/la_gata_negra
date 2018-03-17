init:
    python:
        #item declarations go down here
        blue_key=thing(name="Blue key", description="Just a regular key.", image="key_%s.png", action="item_city")
    image bg black = "#000"






label start:
    jump home

label home:
    "klok"
    jump mainloop

label city:
    "dime ab"
    jump mainloop
