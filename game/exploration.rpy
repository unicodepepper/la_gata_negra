label mainloop:
    python:
        if events[currplace]: #if there's an event, execute it. also let the event call bgshow/advance if it needs
            currjump = events[currplace] 
            events[currplace] = None #clear the event (note - the event can reverse this by setting itself up again)
            renpy.call(label=currjump) #run the event
#
#
        else:   #if there's no event, make the player choose where to go or whta backpack item to use.
            menulist=[("Open the backpack","__backpack_label")] #this placeholder label should only be used inside this mainloop
            for i in connections[currplace]: #all the places i can go from the current place (see script.rpy)
                menulist.append(("Go to the "+location_names[i],i))
            menulist.append(("Stay here",currplace))
            currjump=renpy.display_menu(menulist,screen="choice")
#
            # if the player chose to open their backpack, open their backpack
            if currjump=="__backpack_label": #still no clue how to do private vars in renpy
                currjump=renpy.call_screen("backpack") #@ backpack.rpy #todo: change the backpack list to be passed instead of global
                if currjump=="__back": #clicking the "back" button on the backpack menu
                    renpy.jump("mainloop") #if a backpack item sets up an event in the current location, 
                                            #this will result in the event being triggered immediately. 
                else:
                    renpy.call(label=currjump) 
            else:
                # if the player Did Not chose to open the backpack, go to the place they picked, but Do Not jumpto a label.
                currplace=currjump 
                renpy.call(label='bgshow') #pretty background with no time advance 
                ## 2020-04-19: ^^ this should probably be handled by the event itself, not by the mainloop.
                ## sure, it adds some boilerplate (along with resetting itself in the case of events that are repeated)
                ## but it adds the freedom not to showw it if needded. 
    jump mainloop
