#SCENE 1: MC SELF INTRO

label start:
python:
    name = renpy.input("To start, please enter a name.")
    name = name.strip()
define mc = Character("[name]")
define cl = Character ("Client 1")

mc "insert lore"

#SCENE 2: WORK LOG
scene bg office

mc "My first day! I met a  client!!"
mc "My life is not doomed!!"
mc "Now, let's get back to work..."

#click logbook choice
menu:
    "Open logbook":
        jump logbook

#logbook
label logbook:
    mc "Hmm..."

    #SCENE 3: FLASHBACK
    "Earlier that day..."
    mc "No one's knocking yet... It's been hours since I opened.."
    mc "Did I flo"






 