#SCENE 1: MC SELF INTRO

label start:
python:
    name = renpy.input("To start, please enter a name.")
    name = name.strip()
define mc = Character("[name]")

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
   screen text_example():
    frame:
        xalign 0.5 ypos 50
        text "This is a text displayable.":
            size 30
 