

# Does AlphaMask work on entire layers, instead of just in pictures?
## I don't think it works with layers, but i can create a pseudo-layer
## using a contains statement

# this looks like i could do something cool with it:
#   https://www.renpy.org/doc/html/displayables.html#DynamicDisplayable
## seems like it works just like custom transforms, except it returns 
## an actual displayable insteadof 
# also probably check out user-defined displayables? 

# label intro?:
#     menu:
#         "Have you ever taken a longer route when walking just to avoid running into a pigeon?"
#         "Yes":
#             pass
#         "No":
#             pass
#         "What?"

#     menu:
#         "Was it out of kindness, or out of fear?"
        


init -20 python:
    rspeed=1
    def rotate_func(d,st,at):
        d.rotate=st*rspeed
        d.xalign=0.5
        d.yalign=((st/5)%1)
        return(0)

image blue=Solid("0af", xysize=(90,300))

image blue_anim:
    # This is defined as a separate image with a `contains` so that
    # it has a size of zero. 
    # That's useful for the alphamask, since it will adapt to the size
    # of the full picture. 
    #  
    # not actually useful for images you'll show normally because this 
    # breaks all the align and anchor statements. 
    contains:
        Transform('blue', function=rotate_func)

image blessed:
    size (237,578)
    contains:
        "blessed_shadow.png"
    contains:
        "blessed_outline.png"
    contains:
        "blessed_silhouette.png"
    contains:
        AlphaMask("blue_anim","blessed_silhouette.png")







init python hide:

    class KonamiListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_UP,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_b,
                pygame.K_b,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    # Create a KonamiListener to actually listen for the code.
    store.konami_listener = KonamiListener('konami_code')

    # This adds konami_listener to each interaction.
    def konami_overlay():
        ui.add(store.konami_listener)

    config.overlay_functions.append(konami_overlay)


# This is called in a new context when the konami code is entered.
label konami_code:

    "You just earned an additional 30 lives!"

    "While they might not be of much use in a dating sim, good for you!"

    return