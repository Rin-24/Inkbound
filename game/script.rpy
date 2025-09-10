#reminder (for later): make a label for each client for organization
image journal_anim:
    "book f1.png"
    0.1
    "book f2.png"
    0.1
    "book f3.png"
    0.1
    "book f4.png"
    0.1
    "book f5.png"
    0.1
    "book f6.png"
    0.1
    "book f7.png"
    0.1
    "book f8.png"
    0.1
    "book f9.png"
    0.1
    "book f10.png"
    0.1
    "book f11.png"
    0.1
    "book f12.png"
    5

default score = 0
default total_score = 0
default letter_1 = ""
default letter_2 = ""
default letter_3 = ""
default letter_4 = ""
default letter_5 = ""
default letter_6 = ""
default letter_7 = ""
define gui.text_color = "#000000"

#letter
style letter_window is default:
    xalign 0.5
    yalign 0.5
    xsize 800
    ysize 600
    padding (30, 30)
    text_align 0.0

style letter_text is default:
    color "#000000"
    justify True
    size 30  

screen letter_display():
    add "letter_pic" at truecenter

    window style "letter_window":
        text "[letter_1]\n\n    [letter_2][letter_3][letter_4][letter_5][letter_6][letter_7]" style "letter_text" xalign 0.5


#rating scene
image floating_star:
    "star.png"
    linear 1.5 ypos -100 alpha 0.0

#score display
screen score_display():
    hbox:
        align(0.95,0.05) #top-right
        spacing 10
        add "star.png" size (100,100)
        vbox:
            yalign 0.5
            text "[total_score]" size 48 color "#ffffff" outlines [(1,"#000000",0,0)]
image letter_pic = "letter pic.png"


#splash screen
image splash = "splash.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(0.5)

    return



label start:
    #MC SELF INTRO
    #scene bg room             #the bedroom bg

    $ name_cl = "Client 1"
    $ name_cl2 = "Client 2"

    define mc = Character("[name]", color = "#d94214")         #color based on mc's color palette
    define cl1 = Character ("Client 1", color = "#511d33")     #color based on cl1's color palette
    define cl2 = Character ("Client 2", color = "#050e59")     #color based on cl2's color palette
    
    "The last thing I remember..."
    "and the first thing I saw.. was darkness"
    "Blank and empty. An oddly comforting darkness"
    "I woke up in a strange place, surrounded by paper and pens."
    scene bg room
    "And somehow, it felt familiar"
    "Like a life I've known all along"
    "I tried to retrace my memories. My life. My name..."
    $ name = renpy.input ("What was my name?")
    $ name = name.strip()
    if not name:         
        $ name = "Ash"
    
    show mc base center with dissolve
    mc "Well... no use in searching for blank pages."
    mc "I guess I'll just have to stay here...and figure things out."
    mc "Gather the pieces - guided and bound by ink."
    hide mc base center

    #TUTORIAL
    call screen tutorial_screen(0)
    show screen score_display

    call client_1
    call client_2
    return

'''
    show screen score_display
     #click logbook choice
    menu:
        "Open logbook":
            call logbook        #using call here para makabalik to this point once it reaches the return statement sa logbook 

label logbook:
    #show client 1 profile
    show journal_anim at truecenter
    mc "Hmm..."
    hide journal_anim
    return
'''

label write_letter:
    show screen letter_display
    pause
    hide screen letter_display

    return


screen feedback(score):
    if score == 7:
        add "five stars.png" at truecenter
    elif score >= 5:
        add "four stars.png" at truecenter
    elif score >= 3:
        add "three stars.png" at truecenter
    elif score == 2:
        add "two stars.png" at truecenter
    else:
        add "one star.png" at truecenter

screen cl2_answers:
    frame:
        xsize 1180
        ysize 680
        xalign 0.5
        yalign 0.5
        padding (40,40,25,50)
        has vbox

        text "{size=+12}Answers and Explanations{/size}{vspace=10}" xalign 0.5

        viewport id "ans":
            draggable True
            mousewheel True
            scrollbars "vertical"
            ysize 600
            
            has vbox
            text "1. Standard Cover Letter Greetings: \n{b}{color=#818063}Dear Mrs. XYZ{/color}{/b} / To whom it may concern{vspace=2}"
            text "“To whom it may concern” sounds generic and outdated, which isn’t what the client wants. Using “Dear Mrs. XYZ” sounds more personal and fits the disposition of the client better.{vspace=10}"
            
            text "2. Appropriate Tone: \n This job looks super cool and I think I’d vibe well with the team. / {b}{color=#818063}This opportunity deeply aligns with my goals and values.{/color}{/b}{vspace=2}"
            text "Even though the client wants the letter to show their upbeat character, a cover letter should still be professional and formal.{vspace=10}"

            text "3. Grammar: \nMy experiences ( {b}{color=#818063}align{/color}{/b} / aligns ) with your organization’s mission.{vspace=2}"
            text "“Experiences” is plural, so by subject-verb agreement, “align” should be used.{vspace=10}"

            text "4. Grammar: \nI ( lead / {b}{color=#818063}led{/color}{/b} ) multiple campaigns promoting composting and sustainability in urban neighborhoods.{vspace=2}"
            text "Since it happened in the past, “led” should be used, as the past tense of “lead”.{vspace=10}"

            text "5. Grammar: \nI am familiar with local environmental regulations and (had / {b}{color=#818063}have{/color}{/b} ) hands-on experience collecting field samples and recording environmental data.{vspace=2}"
            text "Based on tense consistency and context, “have” is more suitable to use than “had”. Inconsistent tenses causes confusion to the client’s ability. Using “have” implies they still remember how to do it.{vspace=10}"

            text "6. Spelling: \nThis role complements my commitment to ( {b}{color=#818063}continuous{/color}{/b} \ continuos ) learning, professional growth, and taking part in impactful, on-the-ground environmental efforts.{vspace=2}"
            text "Proper Spelling.{vspace=10}"

            text "7. Grammar: \nI hope to contribute meaningfully ( {b}{color=#818063}to{/color}{/b} \ with ) your mission and values.{vspace=2}"
            text "The right preposition here is “to”; “with” feels grammatically off and awkward.{vspace=10}"

            textbutton "Back" action Return()
        #position the vertical scrollbar
        vbar:
            value YScrollValue("ans")
    
