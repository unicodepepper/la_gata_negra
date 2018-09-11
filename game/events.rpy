label hexed_intro:
    "I step into the computer lab."
    "There's someone inside it, fiddling with the guts of a computer on a table."
    "It's [h.name], someone who I've been acquainted with for a long time, but have never been really close to."
    "They look up to me."
    h "Hey there."
    h "You might want to knock the next time you enter."
    menu:
        h "You might want to knock the next time you enter."
        "Sorry about that.":
            s "Sorry if I scared you. I'll try to do it next time."
            "[h.name] chuckles."
            h "Don't sweat it. I might just be doing it for your protection."
        "You should lock your door.":
            s "I think you should lock your door, if you really don't want people coming in."
            "[h.name] looks down and chuckles."
            h "You might have a point."
            h "But to be honest, I might be telling you to do it for your own sake."
    h "In any case, I might be interested to know what brings you here."
    s "Oh, about that..."
    if firstvisit == "hexed":
        s "I don't know, I just wanted to kill some time."
        h "I see..."
    else:
        s "See, I really want to write, but I've been having a lot of trouble with motivation lately."
        s "You always seem to have something to keep busy with, so I was curious to know how you did it."
        h "I see..."
        h "That might just be the way my mind works. I have no idea."
        h "Or it might be depression for you. Who knows."
        h "I might not be the most qualified person to make such a guess."
        h "You might want to get that tested."
        h "In any case..."
    h "Maybe you'll enjoy trying what I've been working on lately."
    h "It might help get your mind off things."
    s "That sounds nice."
    s "What is it?"
    h "..."
    h "It might not be ready yet."
    h "You might want to come tomorrow."
    h "Oh, but this might help for now."
    "[h.name] hands me a very old music player."
    $backpack_list.append(music_player)
    $renpy.notify("You got a music player.")
    s "Thank you."
    s "I'll go take a walk, so talk to you later."
    h "Take care, then."
    "..."
    scene bg black with dissolve
    "..."
    "[h.name] is quite an odd person."
    return

label charmed_intro:
    "this is charmed's intro"
    return

label blessed_intro:
    "I walk into the art studio."
    "It's a huge space that has been designated for all kinds of arts - even arts that shouldn't really go together."
    "There's areas for painting, theatre, music, sculpting, even writing."
    "However, there were wet canvases spread over most the floor, so I had to mind my step."
    b "Could you please try not to step on my paintings before they dry?"
    if listeningToMusicPlayer:
        "I took off my headphones and looked towards the voice."
    else:
        "I stopped right on my tracks and looked towards the voice."
    s "Don't worry, they're all okay."
    s "But I'll keep it in mind."
    b "Why did you come here?"
    if firstvisit ==  "blessed":
        s "I've been trying to write for a while, but I haven't been able to."
        s "I thought if I came here I'd be able to get more inspired for it."
    else:
        s "I don't know, I was just looking."
        s "Would you like me to leave?"
        b "Why would I want you to? Aren't all artists siblings?"
    b "Could you come sit besides me?"
    "I tiptoed around some canvases and reached [b.name]."
    b "What about your writing is making you feel distant from it?"
    menu:
        b "What about your writing is making you feel distant from it?"
        "The plot.":
            pass
        "The characters":
            pass
    #add some advice... you know the drill
    if listeningToMusicPlayer:
        listeningToMusicPlayer = False
        #why are you trying to drown your mind out? shouldn't you listen to it?
    return
