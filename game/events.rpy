label test_event:
    'this test event just repeats itself'
    '[clockint] [clockstr]'
    $events[currplace]="test_event"
    call bgshow(advance=True)
    return

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
    else: #add more meat to this shit
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
    #don't think so much, just look at the world
    #there's so much out there
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
        b "Could you come sit besides me?"
        "I tiptoed around some canvases and reached [b.name]."
        b "What about your writing is making you feel distant from it?"
        menu:
            b "What about your writing is making you feel distant from it?"
            "The story.":
                b "..."
                b "What do you think is the purpose of telling a story?"
                s "Uh... I guess to communicate with people."
                b "And what do you want to communicate to them?"
                s "I don't know."
                s "I guess... my own feelings about the world."
                b "Feelings?"
                b "What kind of feelings?"
                s "It's embarrassing to talk about them, you know..."
                b "But won't you be showing them to people with your writing?"
                b "Don't you want to start with me?"
                s "I guess..."
                s "I'd say it's hope, but also loneliness, and... a lot of nostalgia."
                s "But not just nostalgia for things that happened."
                s "Nostalgia for things that never happened, or might have happened, or might happen."
                s "Does that make sense?"
                b "Does it make sense to you?"
                s "I think."
                b "Don't you think that's what really matters?"
            "The characters":
                b "So you have a story, but you don't have characters for it?"
                "I nod for a second, before clarifying."
                s "It's not that I don't have characters, but..."
                s "They all feel really bland and flat to me. It's like there's only a single type of person I can write."
                s "I think I'm just inserting myself in everything, and I have no idea how to change that."
                b "Are they really reflections of you? Or are they reflections of who you think you are?"
                b "Wouldn't someone as deep as you be able to write characters that aren't bland and flat?"
                s "I'm not that deep, though."
                b "Do you think you're not as deep as anyone else?"
                s "..."
                s "Maybe."
    else:
        s "I don't know, I was just looking."
        s "Would you like me to leave?"
        b "Why would I want you to? Aren't all artists siblings?"
        s "I'm not really that much of an artist, though."
        b "Could you come sit besides me?"
        "I hesitated, then tiptoed around some canvases and reached [b.name]."
    b "Could you please hold this for me?"
    "[b.name] handed me a wet paintbrush."
    b "Can you try doing something on that canvas over there?"
    "They gestured towards an empty canvas. I tried to keep the brush in the air, careful not to let it drip."
    s "What would you like me to do?"
    b "What do you feel like doing?"
    "They didn't even look at me. They seemed very focused on the piece in front of them."
    "I shrugged."
    s "I don't feel like doing anything."
    "They stayed silent, and just kept painting."
    if listeningToMusicPlayer:
        $listeningToMusicPlayer = False
        b "Are you afraid of your own mind?"
        s "What do you mean?"
        b "Weren't you drowning it with music by the time you got here?"
        "Indeed, I was. Even though I had taken out my headphones, the place was so silent you could hear their sounds very faintly."
        s "I guess I just get bored."
        b "And what's the problem with that?"
        s "I... don't know."
        s "Sometimes bad thoughts come to my mind when I'm bored."
        b "And that's why you try to avoid all your thoughts?"
        b "If your house was dirty, would you avoid coming to it as well? Or would you make an effort to clean it?"
        s "..."
        s "I should make an effort to clean it, in that case."
        s "But it's hard when you're depressed."
        b "..."
        b "Do you think I could help you with that?"
    b "Why don't you come over here some other time, after I'm done with these paintings?"
    b "Wouldn't it be best if I could give you my full attention?"
    s "Yeah, you're right..."
    b "You won't leave me waiting, right?"
    s "No, I won't."
    return



label cat_story:
    b "There was once a cat who really loved apples."
    b "Red apples, green apples, sweet apples, sour apples, big apples, small apples..."
    b "No matter what kind, they had a great taste for them."
    b "They could tell what apples were good or bad at a glance."
    b "Every day, as soon as the sun rose, they would walk out of their house and into the fields around it."
    b "The fields were, of course, full of apple trees. But most of them were your average, everyday apples."
    b "They were looking for the greatest ones. The best of the best. And they found them."
    b "They found one. They found two. They found ten."
    b "Sometimes their rabbit friend would find great ones for them too, as a gift."
    b "They would hold any especially nice apple they got, and admire the beauty of its skin."
    b "\"Oh, this is amazing! I love this one!\", they would say to themselves."
    b "I can tell it's going to be delicious!"
    b "Sometimes, they would take a bite or two right there. But without fail, they would stick it right into a basket and continue looking."
    b "When the sun was setting and their basket was full, the cat would head back home."
    b "\"I found so many good apples today\", they would think. \"But I am so tired after searching so much.\""
    b "\"I won't enjoy an apple as well as I should when I'm feeling so drained.\""
    b "Then they would carefully put the apples away and eat plain potatoes before sleeping."
    b "As the days went by, their house was getting fuller and fuller with apples."
    b "They were having a hard time even walking around!"
    b "But every morning without fail, they would go out to search for more apples."
    b "And every evening without fail, they'd save the apples for later, eat potatoes and fall asleep."
    b "\"I love apples so much\", the cat said to their rabbit friend. \"But I never get to eat them.\""
    b "The rabbit, of course, thought the cat had no reason to be this sad."
