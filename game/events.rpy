label strange_home_intro:
    a "BZZZZT"
    a "Good morning, scientists. It is now 6 AM"
    a "We know the antarctic winter is unforgiving, and we appreciate your research effort."
    a "Your next shipment of supplies is underway and should be arriving later today."
    a "We hope life is treating you well."
    a "This has been your transmission from Management for today."
    a "BZZZZT"

    "Every single fiber in my body wants me to stay in bed."
    "But warmth is treacherous and vile."
    "Without a blanket to take off, I sit up in bed."
    "Despite my ever-present exhaustion, I feel a sense of pride from looking at the workshop I've been living in since the past few weeks."
    "Everything is neat, tidy, clean and organized - as it should be."
    "..."
    "Now that I think about it, this is the first time there's a supply shipment since I've been there."
    "I better check with the other scientists to see how that's actually done. There must be something I can help with."
    $events["labo"]="strange_home_intro"
    $events["track"]="strange_home_intro"
    $events["astro"]="strange_home_intro"
    $events["city"]="city_intro"
    return

label city_intro:

    return

label hexed_labo_intro:
    "I feel the door to the computer lab push drag some equipment on the ground as I swing it open."
    h "Hey, careful..."
    "The voice came from a figure hunched over another even more complicated piece of equipment, fiddling with it."
    s "Sorry about that, hexed."
    h "I'm busy. What are you doing here?"
    s "Do you know about the supply drop that's coming today?"
    h "Ah, right."
    h "Charmed usually takes care of those. I prefer to leave them to it."
    h "She brings them over to the observatory where the storage area is."
    h "Actually, now that I think about it..."
    "Hexed drops their tools and gets up on their crutches."
    h "I had some supplies I wanted to pick up for myself from the storage area. Do you want to join?"
    menu:
        h "I had some supplies I wanted to pick up for myself from the storage area. Do you want to join?"
        "Sure, let's visit the storage area":
            pass
        "No, thanks - I'll go check out the supplies":
            pass
    return

label charmed_track_intro:
    return
label blessed_astro_intro:
    return

